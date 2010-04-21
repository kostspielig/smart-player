#!/usr/bin/python

__id__ = "$Id: Movement.py $"
__version__ = "$Revision: 1 $"
__date__ = "$Date: 20/04/2010 Sat  $"
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

class Mov:
    
    def __init__ (self):
        self.mechNumber = None
        ## Type of movement: Inmovil, Andar, Correr, Saltar
        self.movType = []

    
    def readMov (self, fileName):

        try:
            file = open(fileName, "r")
        except IOError:
            print "The file "+ fileName+ " does not exist"
            return -1
                    
        file.readline()# Read Magic Number : movSBT

        self.mechNumber = int( file.readline() )
        for x in range(self.mechNumber):
            self.movType.append ( file.readline()[0:-2] )
     
        file.close()

    def printMov (self, fileName= "out.txt"):

        file = open(fileName, "w")
                    
        file.write ("movSBT\n")
        file.write (str ( self.mechNumber ) +"\n" )

        for i in range( self.mechNumber ):
            file.write ( str( self.movType[i] ) +"\n" )

        file.close()

