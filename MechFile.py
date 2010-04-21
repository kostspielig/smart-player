#!/usr/bin/python

__id__ = "$Id: MechFile.py $"
__version__ = "$Revision: 2 $"
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
        self.actualMech = int( re.findall(r'[0-9]+', fileName)[0] )

        
        for i in range(self.mechNumber):
            m = Mech.Mech()
            m.playerNumber = int ( file.readline() )
            m.operative = str2bool ( file.readline() )
            m.disconnected = str2bool ( file.readline() )
            m.blocked = str2bool ( file.readline() )
            m.ground = str2bool ( file.readline() )
            m.cell = str ( file.readline()[0:-2] )
            m.facingSide = int ( file.readline() )
            m.facingTorsoSide = int ( file.readline() )
            m.temp = int ( file.readline() )
            m.burning = str2bool ( file.readline() )
            m.stick = str2bool ( file.readline() )
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
                m.conscious = str2bool ( file.readline() )
                for l in range(78):
                    m.impactedSlots[l] = str2bool(file.readline())
                for n in range(8):
                    m.locationsGunFired[n] = str2bool( file.readline() )
                m.ammunitionNumber = int ( file.readline() )
                ##Para cada una de las municiones preparadas para ser expulsadas
                if m.ammunitionNumber > 0:
                    for p in range(m.ammunitionNumber):
                        # Location of the ammunition
                        m.ammunition[p].append(file.readline()[0:-2]) 
                        # Ammunition slot inside the location
                        m.ammunition[p].append(file.readline()[0:-2]) 
            ## End
            for o in range(self.mechNumber):
                m.narc.append( str2bool( file.readline() ) )
            for r in range(self.mechNumber):
                m.inarc.append( str2bool( file.readline() ) )

            ## Add a new mech to the mechSet
            self.mechSet.append(m)
            m = None
        file.close()

               
    def printMechFile (self, filename = "out.txt"):
        f = open (filename, "w")
        f.write ("mechsSBT\n")
        f.write ( str( self.mechNumber )+"\n")
        
        for i in range(self.mechNumber):
            
            f.write (str( self.mechSet[i].playerNumber ) +"\n")
            f.write (str( self.mechSet[i].operative ) +"\n")
            f.write (str( self.mechSet[i].disconnected ) +"\n")
            f.write (str( self.mechSet[i].blocked  ) +"\n")
            f.write (str( self.mechSet[i].ground ) +"\n")
            f.write (str( self.mechSet[i].cell  ) +"\n")
            f.write (str( self.mechSet[i].facingSide  ) +"\n")
            f.write (str( self.mechSet[i].facingTorsoSide  ) +"\n")
            f.write (str( self.mechSet[i].temp  ) +"\n")
            f.write (str( self.mechSet[i].burning  ) +"\n")
            f.write (str( self.mechSet[i].stick  ) +"\n")
            f.write (str( self.mechSet[i].stickType  ) +"\n")
            for j in range(11):
                f.write (str( self.mechSet[i].armorPoints[j] ) +"\n")
            for k in range(8):
                f.write (str( self.mechSet[i].internalStructurePoints[k] ) +"\n")
            ## Is the actual battleMech??
            if self.actualMech == self.mechSet[i].playerNumber:
                f.write (str( self.mechSet[i].walk ) +"\n")
                f.write (str( self.mechSet[i].run ) +"\n")
                f.write (str( self.mechSet[i].jump ) +"\n")
                f.write (str( self.mechSet[i].radiatorsOn ) +"\n")
                f.write (str( self.mechSet[i].radiatorsOff ) +"\n")
                f.write (str( self.mechSet[i].wounds ) +"\n")
                f.write (str( self.mechSet[i].conscious  ) +"\n")
                for l in range(78):
                    f.write (str( self.mechSet[i].impactedSlots[l] ) +"\n")
                for n in range(8):
                    f.write (str( self.mechSet[i].locationsGunFired[n] ) +"\n")
                f.write (str( self.mechSet[i].ammunitionNumber  ) +"\n")
                ##Para cada una de las municiones preparadas para ser expulsadas
                if self.mechSet[i].ammunitionNumber > 0:
                    for p in range(self.mechSet[i].ammunitionNumber):
                        # Location of the ammunition
                        f.write (str( self.mechSet[i].ammunition[p]) +"\n")
                        # Ammunition slot inside the location
                        f.write (str( self.mechSet[i].ammunition[p]) +"\n")
                        
            ## End
            for o in range(self.mechNumber):
                f.write (str( self.mechSet[i].narc[o] ) +"\n")
                
            for r in range(self.mechNumber):
                f.write (str( self.mechSet[i].inarc[r] ) +"\n")
                

            ## End

        f.close()

def str2bool(string):
    return string.strip().lower() in ('yes', '1', 'true')
