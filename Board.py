#!/usr/bin/python

__id__ = "$Id: Board.py $"
__version__ = "$Revision: 1 $"
__date__ = "$Date: 16/04/2010 Fri  $"
__author__ = "Maria Carrasco Rodriguez, Francisco Manuel Herrero Perez"
__license__ = "GPL"
__URL__ = "http://code.google.com/p/smart-player/"

LOGO = """
   _____                      _   _____  _                       
  / ____|                    | | |  __ \| |                      
 | (___  _ __ ___   __ _ _ __| |_| |__) | | __ _ _   _  ___ _ __ 
  \___ \| '_ ` _ \ / _` | '__| __|  ___/| |/ _` | | | |/ _ \ '__|
  ____) | | | | | | (_| | |  | |_| |    | | (_| | |_| |  __/ |   
 |_____/|_| |_| |_|\__,_|_|   \__|_|    |_|\__,_|\__, |\___|_|   
                                                  __/ |          
                                                 |___/            
"""
logo = """
 __             _                
(_ __  _  ___|_|_) |  _  \/ _  __
__)|||(_| |  |_|   | (_| / (/_ | 

"""


import Cell
from math import fabs
from pathfinder import Pos

class Board(object):
    
    def __init__ (self, enemysCell = []):
        self.__width = 0
        self.__height = 0
        self.map = []
        self.enemysCell = enemysCell
        
    def getWidth(self):
        return self.__width

    def setWidth(self, width):
        if isinstance(width, int) and width >= 0:
            self.__width = width
        else:
            print "Error!"
    width = property(getWidth, setWidth)
    
    def getHeight(self):
        return self.__height

    def setHeight(self, height):
        if isinstance(height, int) and height >= 0:
            self.__height = height
        else:
            print "Error!"
    height = property(getHeight, setHeight)
    
    def readBoard (self, fileName):
        """ 
        Reads a board from a specified file 
        
        Arguments:
        * fileName -- Path to the file containing the board description
        
        """

        try:
            file = open(fileName, "r")
        except IOError:
            print "The file "+ fileName+ " does not exist"
            return -1
        
        file.readline() #Leer mapaSBT
        
        self.__height = int( file.readline() )
        self.__width = int( file.readline() )
        
        self.map = [[0] * self.__width for i in range(self.__height)]
        cellNumber = range(self.__width * self.__height)
        faceParams = range (6)
        for x in cellNumber:
            cell = Cell.Cell()       
            col =(x%self.__height)
            fil = (x//self.__height)
            cell.x = col + 1
            cell.y = fil + 1
            cell.level = int( file.readline() )
            cell.ground = int( file.readline() )
            cell.objects = int( file.readline() )
            cell.fce = int( file.readline() )
            cell.collapsedBuilding = str2bool( file.readline() )
            cell.fire = str2bool( file.readline() )
            cell.smoke = str2bool( file.readline() )
            cell.stick = int( file.readline() )
            
            for y in faceParams:
                cell.faceRiver.append(str2bool( file.readline()) )
            
            for y in faceParams:
                cell.faceRoad.append(str2bool( file.readline()) )
                
            self.map[col][fil] =cell
            cell = None
            
        file.close()
        
    def printBoard (self, filename = "out.txt"):
        """ Prints a file text with the map
        contained in the Board
        """
        f = open (filename, "w")
        f.write ("mapaSBT\n")
        f.write ( str( self.__width )+"\n")
        f.write ( str( self.__height)+"\n") 
        
        cellNumber = range(self.__width * self.__height)
        faceParams = range (6)
        for x in cellNumber:
            fil = x%self.__height  # X
            col = x//self.__height # Y
            f.write (str( self.map[fil][col].level ) +"\n")
            f.write (str( self.map[fil][col].ground) +"\n")
            f.write (str( self.map[fil][col].objects) +"\n")
            f.write (str( self.map[fil][col].fce) +"\n")
            f.write (str( self.map[fil][col].collapsedBuilding) +"\n")
            f.write (str( self.map[fil][col].fire) +"\n")
            f.write (str( self.map[fil][col].smoke) +"\n")
            f.write (str( self.map[fil][col].stick)  +"\n")
            
            for y in faceParams:
                f.write (str ( self.map[fil][col].faceRiver[y]) +"\n")
            
            for y in faceParams:
                f.write (str ( self.map[fil][col].faceRoad[y]) +"\n")
          	
        f.close()
        
    def move_cost(self, c1, c2, movType = 0):
        """ Compute the cost of movement from one coordinate c1 to
        another c2. Both coordinates must be adjacent.
        movType 0-walk; 1-run; 2-jump
        """
        p1 = c1.pos
        p2 = c2.pos
        face = 0
        costFace = 0
        costCell = 0
        if movType == 0 or movType == 1:
            face = facing_side(p1, p2)
            # Total cost of changing the facing side
            costFace = min( (c1.face - face)%6, (face - c1.face)%6 )
            difLevel = abs(self.map[p1[0]][p2[1]].level - self.map[p2[0]][p2[1]].level)            
            obj = self.map[p2[0]][p2[1]].objects
            if (self.map[p2[0]][p2[1]].ground == 2): # Agua
                if (self.map[p2[0]][p2[1]].level == -1):
                    costCell = 2
                elif (self.map[p2[0]][p2[1]].level <= -2):
                    costCell = 4
                elif difLevel == 2:
                    costCell = 2
                else:
                    costCell = 1
            elif ( (obj == 3) or (obj== 0) or (obj==1) ): # Escombros o edif pequenios o bosque ligero
                costCell = 2
            elif ((obj == 4) or (obj == 2)): # edif medianos o bosque denso
                costCell = 3
            elif (self.map[p2[0]][p2[1]].objects == 5): # edif grandes
                costCell = 4
            elif (self.map[p2[0]][p2[1]].objects == 6): # edif reforzados
                costCell = 5

            if difLevel  == 2 and self.map[p2[0]][p2[1]].ground != 2: 
                costCell += 2
            elif self.map[p2[0]][p2[1]].ground != 2:
                costCell += 1
        elif movType == 2: # if salto, only 1 PM
            costCell = 1
        return (int(costFace+costCell), face)



    def successors (self, c, movType = 0, PM =15):
        """ Compute the successors of coordinate 'c': all the 
        coordinates that can be reached by one step from 'c'.
        """
        slist = []
        
        # Go over every cell attached
        for i in (-1,0,1):
            for j in (-1,0,1):
                if ((c[1]+1)%2 == 0): #columnas pares
                    if (i == -1 and j == -1) or (i == 0 and j == 0) or (i == 1 and j == -1):
                        continue
                else:
                    if (i == 1 and j == 1) or (i == 0 and j == 0) or (j == 1 and i == -1):
                        continue
                newFil = (c[0]) +j
                newCol = (c[1]) +i

                # Check if we dont try a position out of the board
                if (0 <= newFil <= self.__height -1 and 0 <= newCol <= self.__width -1):
                    
                    #Checks whether the cell is correct
                    if ( self.checkCell(c, (newFil,newCol), movType, PM) ):
                        slist.append((newFil, newCol))

        return slist


    
    def checkCell (self, c1, c2, moveType = 0, PM =15):
        """ Checks whether a cell is allowed to be moved to
        From c1 to c2
        moveType: 0-Walk, 1-Run, 2-Jump
        """
        what = False
        # If running -> water with depth less than one
        if (self.map[c1[0]][c1[1]].level < -1 and moveType == 1):
            return False
        # We do not wanna go through a cell with fire! (running or walking)
        if (self.map[c1[0]][c1[1]].fire == True and moveType == 1 and moveType == 0):
            return False
        # Checks the height difference for run and walk
        if ( abs( self.map[c1[0]][c1[1]].level - self.map[c2[0]][c2[1]].level ) <= 2
             and (moveType == 0 or moveType == 1)):
            what = True
        # Checks whether the height difference is greater than PM
        if ( abs( self.map[c1[0]][c1[1]].level - self.map[c2[0]][c2[1]].level ) <= PM
             and moveType == 2):
            what = True
        #if (self.enemysCell != [] ):
        if c2 in self.enemysCell: 
            return False

        return what


    def heuristic_to_goal_manhatan(self, c1, c2): 
        """ Heuristic 1 - Manhatan
        C1 and C1, Type Pos
        return Distance
        """
        return abs(c2.pos[0]-c1.pos[0]) + abs(c2.pos[1]-c1.pos[1])

    def heuristic_to_goal (self,c1,c2):
        """ Heuristic 2 - Actual distance in a hexagonal grid
        C1 and C1, Type Pos
        return Distance
        """
        p1 = (c2.pos[1]+1, c2.pos[0]+1)
        p2 = (c1.pos[1]+1, c1.pos[0]+1)
        Vx = abs(c2.pos[0]-c1.pos[0])
        Vy = abs(c2.pos[1]-c1.pos[1])
        if Vy%2 != 0:
            factor = 0
        elif c1.pos[1] < c2.pos[1]: 
            factor = (c1.pos[0]-1)%2
        else:
            factor = (c2.pos[0]-1)%2

        return Vx + max(0, Vy- (Vx/2) - factor)
    

def str2bool(string):
    if string.strip().lower() in ('yes', '1', 'true', 'si'):
        return True
    elif string.strip().lower() in ('no', '0', 'false'):
        return False
    else:
        return "Error: Not boolean"

def manhatan (c1,c2):
    return abs(c2[0]-c1[0]) + abs(c2[1]-c1[1])


def facing_side (p1, p2):
    y = - (p1[0] - p2[0])
    x = - (p1[1] - p2[1])
    face = 0 
    if ((p1[1]+1)%2 == 1): #columnas impares
        # Which side is facing the other node??
        if (x == 0 and y == -1): # N
            face = 0
        elif (x == 1 and y == -1): # NE
            face = 1
        elif (x == 1 and y == 0): # SE
            face = 2
        elif (x == 0 and y == 1): # S
            face = 3
        elif (x == -1 and y == 0): # SO
            face = 4
        elif (x == -1 and y == -1): # NO
            face = 5
    else: #columnas pares
        if (x == 0 and y == -1): # N
            face = 0
        elif (x == 1 and y == 0): # NE
            face = 1
        elif (x == 1 and y == 1): # SE
            face = 2
        elif (x == 0 and y == 1): # S
            face = 3
        elif (x == -1 and y == 1): # SO
            face = 4
        elif (x == -1 and y == 0): # NO
            face = 5
    return face

def adjacent_cells (p, face, board):
    """ Returns the adjacent cell of p1 in the side face
    """
    r1 = 0; r0 = 0
    if ((p[1]+1)%2 == 1): #columnas impares
        if face == 0: # N
            r0 = p[0] -1
            r1 = p[1] 
        elif face == 1: # NE
            r0 = p[0] -1
            r1 = p[1] +1
        elif face == 2: # SE
            r0 = p[0] 
            r1 = p[1] +1
        elif face == 3: # S
            r0 = p[0] +1
            r1 = p[1] 
        elif face == 4: # SO
            r0 = p[0] 
            r1 = p[1] -1
        elif face == 5: # NO
            r0 = p[0] -1
            r1 = p[1] -1
    else: #columnas pares
        if face == 0: # N
            r0 = p[0] -1
            r1 = p[1] 
        elif face == 1: # NE
            r0 = p[0] 
            r1 = p[1] +1
        elif face == 2: # ES
            r0 = p[0] +1
            r1 = p[1] +1
        elif face == 3: # S
            r0 = p[0] +1
            r1 = p[1] 
        elif face == 4: # SO
            r0 = p[0] +1
            r1 = p[1] -1
        elif face == 5: # NO
            r0 = p[0] 
            r1 = p[1] -1

    # Check if we dont try a position out of the board
    if (0 <= r0 <= board.height -1 and 0 <= r1 <= board.width -1):
        return r0,r1
    return 0
        


def areAdjacent(c,c2):   
    """ Returns whether 2 cells are adjacent or not """
    slist=[]
    for i in (-1,0,1):
        for j in (-1,0,1):
            if ((c[1]+1)%2 == 0): #columnas pares
                if (i == -1 and j == -1) or (i == 0 and j == 0) or (i == 1 and j == -1):
                    continue
            else:
                if (i == 1 and j == 1) or (i == 0 and j == 0) or (j == 1 and i == -1):
                        continue
            newFil = (c[0]) +j
            newCol = (c[1]) +i

            slist.append((newFil, newCol))
    return c2 in slist
