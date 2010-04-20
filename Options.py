#!/usr/bin/python

__id__ = "$Id: Options.py $"
__version__ = "$Revision: 1 $"
__date__ = "$Date: 17/04/2010 Sat  $"
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
        self.criticalImpact = None
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

        self.fire = str2bool( file.readline() )
        self.wind = str2bool (file.readline() )
        self.windDirection = int (file.readline() )
        self.physicalAttack = str2bool( file.readline() )
        self.heatStage = str2bool( file.readline() )
        self.collapsedForest = str2bool( file.readline() )
        self.collapsedBuilding = str2bool( file.readline() )
        self.pilotCheck = str2bool( file.readline() )
        self.damageCheck = str2bool( file.readline() )
        self.disconnectionCheck = str2bool( file.readline() )
        self.criticalImpact = str2bool( file.readline() )
        self.ammunitionExplosion = str2bool( file.readline() )
        self.offRadiators = str2bool( file.readline() )
        self.timeLimitCheck = str2bool( file.readline() )
        self.timeLimit = str2int (file.readline() )
     
        file.close()

    def printOptions (self, fileName= "out.txt"):

        file = open(fileName, "w")
                    
        file.write("configSBT\n")# Read Magic Number : configSBT

        f.write (str( self.fire ) +"\n")
        f.write (str( self.wind ) +"\n")
        f.write (str( self.windDirection ) +"\n")
        f.write (str( self.physicalAttack ) +"\n")
        f.write (str( self.heatStage ) +"\n")
        f.write (str( self.collapsedForest ) +"\n")
        f.write (str( self.collapsedBuilding ) +"\n")
        f.write (str( self.pilotCheck ) +"\n")
        f.write (str( self.damageCheck ) +"\n")
        f.write (str( self.disconnectionCheck ) +"\n")
        f.write (str( self.criticalImpact ) +"\n")
        f.write (str( self.ammunitionExplosion ) +"\n")
        f.write (str( self.offRadiators ) +"\n")
        f.write (str( self.timeLimitCheck ) +"\n") 
        f.write (str( self.timeLimit ) +"\n")
     
        file.close()

def str2bool(string):
    return string.strip().lower() in ('yes', '1', 'true')
