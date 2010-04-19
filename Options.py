#!/usr/bin/python

__id__ = "$Id: Options.py $"
__version__ = "$Revision: 1 $"
__date__ = "$Date: 17/04/2010 Sat  $"
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

class Options:
    
    def __init__ (self):
        self.fire = None
        self.wind = None
        self.windDirection = None
        self.physicalAttack = None
        self.heatStage = None
        self.collapsedForest = None
        self.collapsedBuilding = None
        self.pilotCheck = None
        self.damageCheck = None
        self.disconnectionCheck = None
        self.criticImpact = None
        self.ammunitionExplosion = None
        self.offRadiators = None
        self.timeLimitCheck = None
        self.timeLimit = None
    
    def readOptions (self, fileName):

        try:
            file = open(fileName, "r")
        except IOError:
            print "The file "+ fileName+ " does not exist"
            return -1
                    
        file.readline()# Read Magic Number : configSBT

        self.fire = bool( file.readline() )
        self.wind = bool (file.readline() )
        self.windDirection = int (file.readline() )
        self.physicalAttack = bool( file.readline() )
        self.heatStage = bool( file.readline() )
        self.collapsedForest = bool( file.readline() )
        self.collapsedBuilding = bool( file.readline() )
        self.pilotCheck = bool( file.readline() )
        self.damageCheck = bool( file.readline() )
        self.disconnectionCheck = bool( file.readline() )
        self.criticImpact = bool( file.readline() )
        self.ammunitionExplosion = bool( file.readline() )
        self.offRadiators = bool( file.readline() )
        self.timeLimitCheck = bool( file.readline() )
        self.timeLimit = int (file.readline() )
     