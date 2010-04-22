#!/usr/bin/python

__id__ = "$Id: DefMech.py $"
__version__ = "$Revision: 1 $"
__date__ = "$Date: 22/04/2010 Thu $"
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

import Dmech
import re

class DefMech:
    
    def __init__ (self):
        self.mechNumber = None
        self.actualMech = None
        self.mechSet = []
        
    def readDefMech (self, fileName):
        """ 
        Read mechs from a specified file 
        
        Arguments:
            * fileName -- Path to the file containing the mechs description
        
        """
        try:
            file = open(fileName, "r")
        except IOError:
            print "The file "+ fileName+ " does not exist"
            return -1

        file.readline() # Read Magic Number : defmetchSBT

        self.name = str ( file.readline() )[0:-2]
        self.model = str ( file.readline() )[0:-2]
        self.actualMech = int( re.findall(r'[0-9]+', fileName)[0] )
