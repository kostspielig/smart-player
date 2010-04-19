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

class Board:
    
    def __init__ (self):
        self.width = None
        self.heith = None
        self.cellArray = []
        
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
        cell = Cell.Cell()
   
        self.width = int( file.readline() )
        self.heith = int( file.readline() )
        
        cellNumber = range(self.width * self.heith)
        faceParams = range (6)
        for x in cellNumber:
            cell.level = int( file.readline() )
            cell.ground = int( file.readline() )
            cell.objects = int( file.readline() )
            cell.fce = int( file.readline() )
            cell.collapsedBuilding = bool( file.readline() )
            cell.fire = bool( file.readline() )
            cell.smoke = bool( file.readline() )
            cell.stick = int( file.readline() )
            
            for y in faceParams:
                cell.faceRiver.append(bool( file.readline()) )
            
            for y in faceParams:
                cell.faceRoad.append(bool( file.readline()) )
          	
          	self.cellArray.append(cell)
          
               
            
                
                
            
        
