#!/usr/bin/python
 
__id__ = "$Id: Initiative.py $"
__version__ = "$Revision:  $"
__date__ = "$Date: 18/05/2010 Fri $"
__author__ = "Maria Carrasco Rodriguez y Francisco Manuel Herrero Perez"
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


class Initiative:
    
    def __init__(self ):
        self.nPlayers = None
        self.position = []

    def readInitiative (self, fileName):

        try:
            file = open(fileName, "r")
        except IOError:
            print "The file "+ fileName+ " does not exist"
            return -1
                    
        self.nPlayers = int ( file.readline() )
        for i in range (self.nPlayers):
            self.position.append( int(file.readline()) )

        file.close()

    def printInitiative (self, filename = "initiative.txt"):
        try:
            f = open (filename, "w")
        except IOError:
            print "Could not open the specified file"
            return -1

        f.write ( str( self.nPlayers )+"\n")
        
        for i in range (self.nPlayers):
            f.write ( str( self.position[i] )+"\n" )

        f.close()


