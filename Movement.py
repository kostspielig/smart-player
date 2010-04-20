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

class Options:
    
    def __init__ (self):
        self.movementType = None
        self.nextCell = None
        self.nextFace = None
        self.masc = None
        self.stepNumber = None
        self.step = []

    
    def readOptions (self, fileName):

        try:
            file = open(fileName, "r")
        except IOError:
            print "The file "+ fileName+ " does not exist"
            return -1
                    
        file.readline()# Read Magic Number : movSBT

        self.fire = str2bool( file.readline() )

     
        file.close()

    def printOptions (self, fileName= "out.txt"):

        file = open(fileName, "w")
                    
        file.write("movSBT\n")

        f.write (str( self.fire ) +"\n")
     
        file.close()

def str2bool(string):
    return string.strip().lower() in ('yes', '1', 'true')
