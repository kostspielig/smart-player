#!/usr/bin/python

__id__ = "$Id: Slot.py $"
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

class Slot(object):
    
    def __init__(self):
        self.__type = None 
        self.__amount = None
        self.__code = None
        self.__name = None
        self.__componentIndex = None
        self.__actuatorIndex = None
        self.__ammunitionDamage = None


    def getType (self):
        return self.__type

    def setType (self, t):
        if isinstance(t, str):
            self.__type = t
        else:
            print "Error, incorrect type!"
    type = property(getType, setType)
 

    def getAmount (self):
        return self.__amount

    def setAmount (self, amount):
        if isinstance(amount, int):
            self.__amount = amount
        else:
            print "Error, incorrect amount!"
    amount = property(getAmount, setAmount)

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
        if isinstance(name, str):
            self.__name = name
        else:
            print "Error, incorrect name!"
    name = property(getName, setName)


    def getComponentIndex (self):
        return self.__componentIndex

    def setComponentIndex (self, componentIndex):
        if isinstance(componentIndex, int):
            self.__componentIndex = componentIndex
        else:
            print "Error, incorrect componentIndex!"
    componentIndex = property(getComponentIndex, setComponentIndex)


    def getActuatorIndex (self):
        return self.__actuatorIndex

    def setActuatorIndex (self, actuatorIndex):
        if isinstance(actuatorIndex, int):
            self.__actuatorIndex = actuatorIndex
        else:
            print "Error, incorrect actuatorIndex!"
    actuatorIndex = property(getActuatorIndex, setActuatorIndex)


    def getAmmunitionDamage (self):
        return self.__ammunitionDamage

    def setAmmunitionDamage (self, ammunitionDamage):
        if isinstance(ammunitionDamage, int):
            self.__ammunitionDamage = ammunitionDamage
        else:
            print "Error, incorrect ammunitionDamage!"
    ammunitionDamage = property(getAmmunitionDamage, setAmmunitionDamage)




