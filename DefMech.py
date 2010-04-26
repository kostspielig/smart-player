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
import Component
import Actuator
import Slot

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

        m = Dmech()
        
        file.readline() # Read Magic Number : defmetchSBT

        m.name = str ( file.readline() )[0:-2]
        m.model = str ( file.readline() )[0:-2]
        m.ton = int ( file.readline() )
        m.power = int ( file.readline() )
        m.internalRadiators = int ( file.readline() )
        m.radiators = int ( file.readline() )
        m.masc = str2bool ( file.readline() )
        m.dacmtd = str2bool ( file.readline() )
        m.dacmti = str2bool ( file.readline() )
        m.dacmtc = str2bool ( file.readline() )
        m.heat = int ( file.readline() )
        m.arms = str2bool ( file.readline() )
        m.lShoulder = str2bool ( file.readline() )
        m.lArm = str2bool ( file.readline() )
        m.lForearm = str2bool ( file.readline() )
        m.lHand = str2bool ( file.readline() )
        m.rShoulder = str2bool ( file.readline() )
        m.rArm = str2bool ( file.readline() )
        m.rForearm = str2bool ( file.readline() )
        m.rHand = str2bool ( file.readline() )
        m.lArmArmor = int ( file.readline() )
        m.lTorsoArmor = int ( file.readline() )
        m.lLegArmor = int ( file.readline() )
        m.rLegArmor = int ( file.readline() )
        m.rTorsoArmor = int ( file.readline() )
        m.rArmArmor = int ( file.readline() )
        m.cTorsoArmor = int ( file.readline() )
        m.headArmor = None
        m.lBackTorsoArmor = int ( file.readline() )
        m.rBackTorsoArmor =  int ( file.readline() )
        m.cBackTorsoArmor = int ( file.readline() )
        m.lInternalArmPoints = int ( file.readline() )
        m.lInternalTorsoPoints = int ( file.readline() )
        m.lInternalLegPoints = int ( file.readline() )
        m.rInternalLegPoints = int ( file.readline() )
        m.rInternalTorsoPoints = int ( file.readline() )
        m.rInternalArmPoints = int ( file.readline() )
        m.cInternalTorsoPoints = int ( file.readline() )
        m.internalHeadPoints = int ( file.readline() )
        m.equippedComponentsNumber = int ( file.readline() )
        for x in range (m.equippedComponentsNumber):
            m.component.append(Component() )
            m.component[x].code = int ( file.readline() )
            m.component[x].name = str ( file.readline() )[0:-2]
            m.component[x].type = str ( file.readline() )[0:-2]
            m.component[x].weaponInBack = str2bool ( file.readline() )
            m.component[x].itemLocation = int ( file.readline() )
            m.component[x].secondaryItemLocation = int ( file.readline() )
            m.component[x].weaponType = str ( file.readline() )[0:-2]
            m.component[x].heat = int ( file.readline() )
            m.component[x].harm = int ( file.readline() )
            m.component[x].shotsPerTurn = int ( file.readline() )
            m.component[x].minimumDistance = int ( file.readline() )
            m.component[x].shortDistance = int ( file.readline() )
            m.component[x].mediumDistance = int ( file.readline() )
            m.component[x].longDistance = int ( file.readline() )
            m.component[x].operativeTeam = str2bool ( file.readline() )
            m.component[x].weaponCode = int ( file.readline() )
            m.component[x].amount = int ( file.readline() )
            m.component[x].specialAmmunition = str2bool ( file.readline() )
            m.component[x].triggerSwitch = int ( file.readline() )

        m.weaponsNumber =  int ( file.readline() )
        m.actuatorsNumber = int ( file.readline() )
        for p in range(m.actuatorsNumber):
            m.actuator.append(Actuator())
            m.actuator[p].code = int ( file.readline() )
            m.actuator[p].name = str ( file.readline() )[0:-2]
            m.actuator[p].itemLocation = int ( file.readline() )
            m.actuator[p].operative = str2bool ( file.readline() )
            m.actuator[p].impactsNumber = int ( file.readline() )
        for v in range(8):
            m.location[v].slotNumber = int ( file.readline() )
            for w in range(m.location[v].slotNumber):
                m.slot.append(Slot())
                m.slot[v].type =  str ( file.readline() )[0:-2]
                m.slot[v].amount = int ( file.readline() )
                m.slot[v].code = int ( file.readline() )
                m.slot[v].name =  str ( file.readline() )[0:-2]
                m.slot[v].componentIndex = int ( file.readline() )
                m.slot[v].actuatorIndex = int ( file.readline() )
                m.slot[v].ammunitionDamage = int ( file.readline() )
                
        m.walkPoints = int ( file.readline() )
        m.runPoints = int ( file.readline() )
        m.jumpPoints = int ( file.readline() )
        m.radiatorsType = int ( file.readline() )


def str2bool(string):
    if string.strip().lower() in ('yes', '1', 'true', 'si'):
        return True
    elif string.strip().lower() in ('no', '0', 'false'):
        return False
    else:
        return "Error: Not boolean"

