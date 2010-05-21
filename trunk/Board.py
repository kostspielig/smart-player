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

class Board(object):
    
    def __init__ (self):
        self.__width = 0
        self.__height = 0
        self.map = []
        
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
   
        self.__width = int( file.readline() )
        self.__height = int( file.readline() )
        
        self.map = [[0] * self.__width for i in range(self.__height)]
        cellNumber = range(self.__width * self.__height)
        faceParams = range (6)
        for x in cellNumber:
            cell = Cell.Cell()       
            cell.x = (x%self.__height) + 1
            cell.y = (x//self.__height) + 1
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
          	
            self.map[cell.x-1][cell.y-1] =cell
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
            


    def move_cost(self, c1, c2):
        """ Compute the cost of movement from one coordinate c1 to
            another c2. 
            
            The cost is the Euclidean distance.
        """
        face = 0
        costFace = 0
        costCell = 0
        #return sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2) 
        x = - (c1[0] - c2[0])
        y = - (c1[1] - c2[1])
        
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
        # Total cost of changing the facing side
        costFace = fabs(c1.face - face) 
            
        if (self.mapa[c2[0]-1][c2[1]-1].ground == 2): # Agua
            if (self.mapa[c2[0]-1][c2[1]-1].level == 1):
                costCell = 2
            elif (self.mapa[c2[0]-1][c2[1]-1].level >= 2):
                costCell = 4
        elif (self.mapa[c2[0]-1][c2[1]-1].objets == (3 or 0 or 1)): # Escombros o edif pequeños o bosque ligero
            costCell = 2
        elif (self.mapa[c2[0]-1][c2[1]-1].objects == (4 or 2)): # edif medianos o bosque denso
            costCell = 3
        elif (self.mapa[c2[0]-1][c2[1]-1].objects == 5): # edif grandes
            costCell = 4
        elif (self.mapa[c2[0]-1][c2[1]-1].objects == 6): # edif reforzados
            costCell = 5

    def successors (self, c, movType = 0):
        """ Compute the successors of coordinate 'c': all the 
            coordinates that can be reached by one step from 'c'.
        """
        slist = []
        # Go over every cell attached
        for i in (-1,0,1):
            for j in (-1,0,1):
                if (i == 1 and j == 1) or (i == 0 and j == 0) or (i == -1 and j == 1):
                    continue
                newi = (c[0] -1) +i
                newj = (c[1] -1) +j
                # Check if we dont try a position out of the board
                if (0 <= newi <= self.__width -1 and 0 <= newj <= self.__height -1):
                    #Checks whether the cell is correct
                    if ():
                        slist.append((newi+1, newj+1))

        return slist


                
    def checkCell (self, c1, c2, moveType = 0):
        """ Checks whether a cell is allowed to be moved to
            From c1 to c2
        """
        what = False
        # If running -> water with depth less than one
        if (abs (self.map[c1[0]][c1[1]].level) > 1 and moveType == 1):
            return False
        # Checks the height difference
        if ( abs( self.map[c1[0]][c1[1]].level - self.map[c2[0]][c2[1]].level ) < 2):
            what = True

        return what

def str2bool(string):
    if string.strip().lower() in ('yes', '1', 'true', 'si'):
        return True
    elif string.strip().lower() in ('no', '0', 'false'):
        return False
    else:
        return "Error: Not boolean"
