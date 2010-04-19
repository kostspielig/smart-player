#!/usr/bin/python
NAME = """
#######################################
   _    _            ___    _ 
  | \  / |    /\    |   \  | |    /\
  |  \/  |   /  \   |   /  | |   /  \
  |  __  |  / __ \  |   \  | |  / __ \
  |_|  |_| /_/  \_\ |_|\_\ |_| /_/  \_\
#######################################
"""

__id__ = "$Id: Mech.py $"
__version__ = "$Revision: 1 $"
__date__ = "$Date: 17/04/2010 Sat  $"
__author__ = "Maria Carrasco Rodriguez y Francisco Manuel Herrero PŽrez"
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

class Mech:
    """ Mech information """

    def __init__ (self):
        self.playerNumber = None
        self.operative = None
        self.disconnected = None
        self.blocked = None
        self.ground = None
        self.cell = None
        self.facingSide = None # [1..6]
        self.temp = None
        self.burning = None
        self.stick = None
        self.stickType = None # [0,1]
        self.armorPoints = []
        for i in range(11):
            self.armorPoints.append(None)
        self.internalStructurePoints = []
        for j in range(8):
            self.internalStructurePoints.append(None)
        ##### Just for some BattleMechs- Actual #####
        self.walk = None
        self.run = None
        self.jump = None
        self.radiatorsOn = None
        self.radiatorsOff = None
        self.wounds = None
        self.conscious = None
        self.impactedSlots = []
        for k  in range(78):
            self.impactedSlots.append(None)
        self.locationsGunFired = []
        for l in range(8):
            self.locationsGunFired.append(None)
        self.ammunitionNumber = None
        self.ammunition = []
        self.ammunition.append(None) # location of the ammunition
        self.ammunition.append(None) # slot in the location
        ##### End #####
        self.narc = None
        self.inarc = None
