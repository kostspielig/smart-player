#!/usr/bin/python

__id__ = "$Id: Location.py $"
__version__ = "$Revision: 1 $"
__date__ = "$Date: 26/04/2010 Mon $"
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

class Location(object):
    
    def __init__(self):
        self.__slotNumber = None 
        self.slot = []


    def getSlotNumber (self):
        return self.__slotNumber

    def setSlotNumber (self, slotNumber):
        if isinstance(slotNumber, int):
            self.__slotNumber = slotNumber
        else:
            print "Error, incorrect slotNumber!"
    slotNumber = property(getSlotNumber, setSlotNumber)
