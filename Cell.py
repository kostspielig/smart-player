#!/usr/bin/python

__id__ = "$Id: Cell.py $"
__version__ = "$Revision: 1 $"
__date__ = "$Date: 16/04/2010 Fri $"
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


class Cell(object):
    
    def __init__(self):
        self.__level = None
        self.__ground = None
        self.__objects = None
        self.__fce = None
        self.__collapsedBuilding = None
        self.__fire = None
        self.__smoke = None
        self.__stick = None
        self.faceRiver = []
        self.faceRoad = []
        
    def getLevel (self):
        return self.__level

    def setLevel (self, level):
        if isinstance(level, int):
            self.__level = level
        else:
            print "Error, incorrect level!"
    level = property(getLevel, setLevel)

        
    def getGround (self):
        return self.__ground

    def setGround (self, ground):
        if isinstance(ground, int) and ground >= 0:
            self.__ground = ground
        else:
            print "Error, incorrect ground!"
    ground = property(getGround, setGround)

    def getObjects (self):
        return self.__objects

    def setObjects (self, objects):
        if isinstance(objects, int) and objects >= 0:
            self.__objects = objects
        else:
            print "Error, incorrect objects!"
    objects = property(getObjects, setObjects)

    def getFce (self):
        return self.__fce

    def setFce (self, fce):
        if isinstance(fce, int) and fce >= 0:
            self.__fce = fce
        else:
            print "Error, incorrect fce!"
    fce = property(getFce, setFce)

    def getCollapsedBuilding(self):
        return self.__collapsedBuilding

    def setCollapsedBuilding (self, collapsedBuilding):
        if isinstance(collapsedBuilding, bool):
            self.__collapsedBuilding = collapsedBuilding
        else:
            print "Error, incorrect collapsedBuilding!"
    collapsedBuilding = property(getCollapsedBuilding, setCollapsedBuilding)

    def getFire (self):
        return self.__fire

    def setFire (self, fire):
        if isinstance(fire, bool):
            self.__fire = fire
        else:
            print "Error, incorrect fire!"
    fire = property(getFire, setFire)

    def getSmoke (self):
        return self.__smoke

    def setSmoke (self, smoke):
        if isinstance(smoke, bool):
            self.__smoke = smoke
        else:
            print "Error, incorrect smoke!"
    smoke = property(getSmoke, setSmoke)

    def getStick (self):
        return self.__stick

    def setStick (self, stick):
        if isinstance(stick, int) and stick >= 0:
            self.__stick = stick
        else:
            print "Error, incorrect stick!"
    stick = property(getStick, setStick)

