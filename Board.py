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

class Board(object):
    
    def __init__ (self):
        self.__width = None
        self.__height = None
        self.cellArray = []
        
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
        
        cellNumber = range(self.width * self.height)
        faceParams = range (6)
        for x in cellNumber:
            cell = Cell.Cell()       
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
          	
            self.cellArray.append(cell)
            cell = None
          
        file.close()
               
    def printBoard (self, filename = "out.txt"):
        f = open (filename, "w")
        f.write ("mapaSBT\n")
        f.write ( str( self.__width )+"\n")
        f.write ( str( self.__height)+"\n") 
        
        cellNumber = range(self.__width * self.__height)
        faceParams = range (6)
        for x in cellNumber:
            f.write (str( self.cellArray[x].level ) +"\n")
            f.write (str( self.cellArray[x].ground) +"\n")
            f.write (str( self.cellArray[x].objects) +"\n")
            f.write (str( self.cellArray[x].fce) +"\n")
            f.write (str( self.cellArray[x].collapsedBuilding) +"\n")
            f.write (str( self.cellArray[x].fire) +"\n")
            f.write (str( self.cellArray[x].smoke) +"\n")
            f.write (str( self.cellArray[x].stick)  +"\n")
            
            for y in faceParams:
                f.write (str ( self.cellArray[x].faceRiver[y]) +"\n")
            
            for y in faceParams:
                f.write (str ( self.cellArray[x].faceRoad[y]) +"\n")
          	
        f.close()
            

def str2bool(string):
    return string.strip().lower() in ('yes', '1', 'true')
