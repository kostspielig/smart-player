#!/usr/bin/python

__id__ = "$Id: MechFile.py $"
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
import Mech
import re

class MechFile:
    
    def __init__ (self):
        self.mechNumber = None
        self.actualMech = None
        self.mechSet = []
        
    def readMechFile (self, fileName):
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

        file.readline() # Read Magic Number : metchsSBT

        self.mechNumber = int ( file.readline() )
        self.actualMech = int( re.findall(r'[0-9]+', s)[0] )

        
        for i in range(self.mechNumber):
            m = Mech.Mech()
            m.playerNumber = int ( file.readline() )
            m.operative = bool ( file.readline() )
            m.disconnected = bool ( file.readline() )
            m.blocked = bool ( file.readline() )
            m.ground = bool ( file.readline() )
            m.cell = int ( file.readline() )
            m.facingSide = int ( file.readline() )
            m.temp = int ( file.readline() )
            m.burning = bool ( file.readline() )
            m.stick = bool ( file.readline() )
            m.stickType = int ( file.readline() )
            for j in range(11):
                m.armorPoints[j] = int ( file.readline() )
            for k in range(8):
                m.internalStructurePoints[k] = int ( file.readline() )
            ## Is the actual battleMech??
            if self.actualMech == m.playerNumber:
                m.walk = int( file.readline() )
                m.run = int( file.readline() )
                m.jump = int ( file.readline() )
                m.radiatorsOn = int ( file.readline() )
                m.radiatorsOff = int ( file.readline() )
                m.wounds = int ( file.readline() )
                m.conscious = bool ( file.readline() )
                for l in range(78):
                    m.impactedSlots[l] = bool(file.readline())
                for n in range(8):
                    m.locationsGunFired[n] = bool( file.readline() )
                m.ammunitionNumber = int ( file.readline() )
            ## End
            for l in range(mechNumber):
                m.narc[l] = bool( file.readline() )
            for h in range(mechNumber):
                m.inarc[h] = bool( file.readline() )

            ## Add a new mech to the mechSet
            self.mechSet.append(m)
            m = None
