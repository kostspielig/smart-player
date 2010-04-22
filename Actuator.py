#!/usr/bin/python

__id__ = "$Id: Actuator.py $"
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


class Actuator(object):
    
    def __init__(self):
        self.__code = None 
        self.__name = None  
        self.__itemLocation = None  
        self.__operative = None  
        self.__impactsNumber = None 


    def getCode (self):
        return self.__code

    def setCode (self, code):
        if isinstance(code, int):
            self.__code = code
        else:
            print "Error, incorrect code!"
    code = property(getCode, setCode)

    def getName (self):
        return self.__name

    def setName (self, name):
        if isinstance(name, int):
            self.__name = name
        else:
            print "Error, incorrect name!"
    name = property(getName, setName)

    def getItemLocation (self):
        return self.__itemLocation

    def setItemLocation (self, itemLocation):
        if isinstance(itemLocation, int):
            self.__itemLocation = itemLocation
        else:
            print "Error, incorrect itemLocation!"
    itemLocation = property(getItemLocation, setItemLocation)

    def getOperative (self):
        return self.__operative

    def setOperative (self, operative):
        if isinstance(operative, int):
            self.__operative = operative
        else:
            print "Error, incorrect operative!"
    operative = property(getOperative, setOperative)

    def getImpactsNumber (self):
        return self.__impactsNumber

    def setImpactsNumber (self, impactsNumber):
        if isinstance(impactsNumber, int):
            self.__impactsNumber = impactsNumber
        else:
            print "Error, incorrect impactsNumber!"
    impactsNumber = property(getImpactsNumber, setImpactsNumber)


   

