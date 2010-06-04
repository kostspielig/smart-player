#!/usr/bin/python

__id__ = "$Id: DefMech.py $"
__version__ = "$Revision: 2 $"
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
       self.mech = Dmech.Dmech()
        
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

        m = Dmech.Dmech()
        
        file.readline() # Read Magic Number : defmechSBT

        m.name = str ( file.readline() ).strip('\n').strip('\r')
        m.model = str ( file.readline() ).strip('\n').strip('\r')
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
        m.headArmor = int ( file.readline() )
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
            m.component.append(Component.Component() )
            m.component[x].code = int ( file.readline() )
            m.component[x].name = str ( file.readline() ).strip('\n').strip('\r')
            m.component[x].type = str ( file.readline() ).strip('\n').strip('\r')
            m.component[x].weaponInBack = str2bool ( file.readline() )
            m.component[x].itemLocation = int ( file.readline() )
            m.component[x].secondaryItemLocation = int ( file.readline() )
            m.component[x].weaponType = str ( file.readline() ).strip('\n').strip('\r')
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
            m.component[x].specialAmmunition = str ( file.readline() ).strip('\n').strip('\r')
            m.component[x].triggerSwitch = int ( file.readline() )

        m.weaponsNumber =  int ( file.readline() )
        m.actuatorsNumber = int ( file.readline() )
        for p in range(m.actuatorsNumber):
            m.actuator.append(Actuator.Actuator())
            m.actuator[p].code = int ( file.readline() )
            m.actuator[p].name = str ( file.readline() ).strip('\n').strip('\r')
            m.actuator[p].itemLocation = int ( file.readline() )
            m.actuator[p].operative = str2bool ( file.readline() )
            m.actuator[p].impactsNumber = int ( file.readline() )
        for v in range(8):
            m.location[v].slotNumber = int ( file.readline() )
            for w in range(m.location[v].slotNumber):
                m.location[v].slot.append(Slot.Slot())
                m.location[v].slot[w].type = str ( file.readline() ).strip('\n').strip('\r')
                m.location[v].slot[w].amount = int ( file.readline() )
                m.location[v].slot[w].code = int ( file.readline() )
                m.location[v].slot[w].name =  str ( file.readline() ).strip('\n').strip('\r')
                m.location[v].slot[w].componentIndex = int ( file.readline() )
                m.location[v].slot[w].actuatorIndex = int ( file.readline() )
                m.location[v].slot[w].ammunitionDamage = int ( file.readline() )
                
        m.walkPoints = int ( file.readline() )
        m.runPoints = int ( file.readline() )
        m.jumpPoints = int ( file.readline() )
        m.radiatorsType = int ( file.readline() )

        self.mech = m


    def printDefMech (self, filename = "out.txt"):
        f = open (filename, "w")
        f.write ("defmechSBT\n")
        f.write ( str( self.mech.name )+"\n")
        f.write ( str( self.mech.model )+"\n")
        f.write ( str( self.mech.ton  )+"\n")
        f.write ( str( self.mech.power )+"\n")
        f.write ( str( self.mech.internalRadiators )+"\n")
        f.write ( str( self.mech.radiators )+"\n")
        f.write ( str( self.mech.masc )+"\n")
        f.write ( str( self.mech.dacmtd )+"\n")
        f.write ( str( self.mech.dacmti )+"\n")
        f.write ( str( self.mech.dacmtc )+"\n")
        f.write ( str( self.mech.heat  )+"\n")
        f.write ( str( self.mech.arms  )+"\n")
        f.write ( str( self.mech.lShoulder )+"\n")
        f.write ( str( self.mech.lArm  )+"\n")
        f.write ( str( self.mech.lForearm )+"\n")
        f.write ( str( self.mech.lHand  )+"\n")
        f.write ( str( self.mech.rShoulder )+"\n")
        f.write ( str( self.mech.rArm  )+"\n")
        f.write ( str( self.mech.rForearm  )+"\n")
        f.write ( str( self.mech.rHand  )+"\n")
        f.write ( str( self.mech.lArmArmor  )+"\n")
        f.write ( str( self.mech.lTorsoArmor )+"\n")
        f.write ( str( self.mech.lLegArmor  )+"\n")
        f.write ( str( self.mech.rLegArmor  )+"\n")
        f.write ( str( self.mech.rTorsoArmor )+"\n")
        f.write ( str( self.mech.rArmArmor  )+"\n")
        f.write ( str( self.mech.cTorsoArmor )+"\n")
        f.write ( str( self.mech.headArmor  )+"\n")
        f.write ( str( self.mech.lBackTorsoArmor  )+"\n")
        f.write ( str( self.mech.rBackTorsoArmor  )+"\n")
        f.write ( str( self.mech.cBackTorsoArmor  )+"\n")
        f.write ( str( self.mech.lInternalArmPoints  )+"\n")
        f.write ( str( self.mech.lInternalTorsoPoints )+"\n")
        f.write ( str( self.mech.lInternalLegPoints  )+"\n")
        f.write ( str( self.mech.rInternalLegPoints  )+"\n")
        f.write ( str( self.mech.rInternalTorsoPoints )+"\n")
        f.write ( str( self.mech.rInternalArmPoints  )+"\n")
        f.write ( str( self.mech.cInternalTorsoPoints )+"\n")
        f.write ( str( self.mech.internalHeadPoints  )+"\n")
        f.write ( str( self.mech.equippedComponentsNumber )+"\n")
        for x in range (self.mech.equippedComponentsNumber):
            f.write ( str( self.mech.component[x].code  )+"\n")
            f.write ( str( self.mech.component[x].name  )+"\n")
            f.write ( str( self.mech.component[x].type  )+"\n")
            f.write ( str( self.mech.component[x].weaponInBack )+"\n")
            f.write ( str( self.mech.component[x].itemLocation  )+"\n")
            f.write ( str( self.mech.component[x].secondaryItemLocation )+"\n")
            f.write ( str( self.mech.component[x].weaponType )+"\n")
            f.write ( str( self.mech.component[x].heat  )+"\n")
            f.write ( str( self.mech.component[x].harm  )+"\n")
            f.write ( str( self.mech.component[x].shotsPerTurn  )+"\n")
            f.write ( str( self.mech.component[x].minimumDistance )+"\n")
            f.write ( str( self.mech.component[x].shortDistance  )+"\n")
            f.write ( str( self.mech.component[x].mediumDistance  )+"\n")
            f.write ( str( self.mech.component[x].longDistance )+"\n")
            f.write ( str( self.mech.component[x].operativeTeam )+"\n")
            f.write ( str( self.mech.component[x].weaponCode )+"\n")
            f.write ( str( self.mech.component[x].amount  )+"\n")
            f.write ( str( self.mech.component[x].specialAmmunition )+"\n")
            f.write ( str( self.mech.component[x].triggerSwitch  )+"\n")

        f.write ( str( self.mech.weaponsNumber  )+"\n")
        f.write ( str( self.mech.actuatorsNumber  )+"\n")
        for p in range(self.mech.actuatorsNumber):
            f.write ( str( self.mech.actuator[p].code  )+"\n")
            f.write ( str( self.mech.actuator[p].name  )+"\n")
            f.write ( str( self.mech.actuator[p].itemLocation )+"\n")
            f.write ( str( self.mech.actuator[p].operative  )+"\n")
            f.write ( str( self.mech.actuator[p].impactsNumber )+"\n")
        for v in range(8):
            f.write ( str( self.mech.location[v].slotNumber  )+"\n")
            for w in range(self.mech.location[v].slotNumber):
                f.write ( str( self.mech.location[v].slot[w].type  )+"\n")
                f.write ( str( self.mech.location[v].slot[w].amount )+"\n")
                f.write ( str( self.mech.location[v].slot[w].code  )+"\n")
                f.write ( str( self.mech.location[v].slot[w].name  )+"\n")
                f.write ( str( self.mech.location[v].slot[w].componentIndex )+"\n")
                f.write ( str( self.mech.location[v].slot[w].actuatorIndex  )+"\n")
                f.write ( str( self.mech.location[v].slot[w].ammunitionDamage  )+"\n")
                
        f.write ( str( self.mech.walkPoints )+"\n")
        f.write ( str( self.mech.runPoints  )+"\n")
        f.write ( str( self.mech.jumpPoints  )+"\n")
        f.write ( str( self.mech.radiatorsType )+"\n")


def str2bool(string):
    if string.strip().lower() in ('yes', '1', 'true', 'si'):
        return True
    elif string.strip().lower() in ('no', '0', 'false'):
        return False
    else:
        return "Error: Not boolean"

