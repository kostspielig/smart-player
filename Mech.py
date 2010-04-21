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
__version__ = "$Revision: 2 $"
__date__ = "$Date: 17/04/2010 Sat  $"
__author__ = "Maria Carrasco Rodriguez , Francisco Manuel Herrero Perez"
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

class Mech(object):
    """ Mech information """

    def __init__ (self):
        self.__playerNumber = None
        self.__operative = None
        self.__disconnected = None
        self.__blocked = None
        self.__ground = None
        self.__cell = None
        self.__facingSide = None # [1..6]
        self.__facingTorsoSide = None
        self.__temp = None
        self.__burning = None
        self.__stick = None
        self.__stickType = None # (0,1)
        self.armorPoints = []
        
        for i in range(11):
            self.armorPoints.append(None)
        
        self.internalStructurePoints = []
        
        for j in range(8):
            self.internalStructurePoints.append(None)
        ##### Just for some BattleMechs- Actual #####
        self.__walk = None
        self.__run = None
        self.__jump = None
        self.__radiatorsOn = None
        self.__radiatorsOff = None
        self.__wounds = None
        self.__conscious = None
        self.impactedSlots = []
        
        for k  in range(78):
            self.impactedSlots.append(None)
        
        self.locationsGunFired = []
        
        for l in range(8):
            self.locationsGunFired.append(None)
        
        self.__ammunitionNumber = None
        self.ammunition = []
        self.ammunition.append(None) # location of the ammunition
        self.ammunition.append(None) # slot in the location
        ##### End #####
        self.narc = []
        self.inarc = []

    def getPlayerNumber (self):
        return self.__playerNumber

    def setPlayerNumber (self, playerNumber):
        if isinstance(playerNumber, int) and playerNumber >= 0:
            self.__playerNumber = playerNumber
        else:
            print "Error, incorrect playerNumber!"
    playerNumber = property(getPlayerNumber, setPlayerNumber)


    def getOperative (self):
        return self.__operative

    def setOperative (self, operative):
        if isinstance(operative, bool):
            self.__operative = operative
        else:
            print "Error, incorrect operative!"
    operative = property(getOperative, setOperative)


    def getDisconnected (self):
        return self.__disconnected

    def setDisconnected (self, disconnected):
        if isinstance(disconnected, bool):
            self.__disconnected = disconnected
        else:
            print "Error, incorrect disconnected!"
    disconnected = property(getDisconnected, setDisconnected)


    def getBlocked (self):
        return self.__blocked

    def setBlocked (self, blocked):
        if isinstance(blocked, bool):
            self.__blocked = blocked
        else:
            print "Error, incorrect blocked!"
    blocked = property(getBlocked, setBlocked)


    def getGround (self):
        return self.__ground

    def setGround (self, ground):
        if isinstance(ground, bool):
            self.__ground = ground
        else:
            print "Error, incorrect ground!"
    ground = property(getGround, setGround)


    def getCell (self):
        return self.__cell

    def setCell (self, cell):
        if isinstance(cell, str):
            self.__cell = cell
        else:
            print "Error, incorrect cell!"
    cell = property(getCell, setCell)


    def getFacingSide (self):
        return self.__facingSide

    def setFacingSide (self, facingSide):
        if isinstance(facingSide, int) and facingSide >=1 and facingSide <= 6:
            self.__facingSide = facingSide
        else:
            print "Error, incorrect facingSide!"
    facingSide = property(getFacingSide, setFacingSide)


    def getFacingTorsoSide (self):
        return self.__facingTorsoSide

    def setFacingTorsoSide (self, facingTorsoSide):
        if isinstance(facingTorsoSide, int) and facingTorsoSide >=1 and facingTorsoSide <= 6:
            self.__facingTorsoSide = facingTorsoSide
        else:
            print "Error, incorrect facingTorsoSide!"
    facingTorsoSide = property(getFacingTorsoSide, setFacingTorsoSide)


    def getTemp (self):
        return self.__temp

    def setTemp (self, temp):
        if isinstance(temp, int) and temp >= 0:
            self.__temp = temp
        else:
            print "Error, incorrect temp!"
    temp = property(getTemp, setTemp)


    def getBurning (self):
        return self.__burning

    def setBurning (self, burning):
        if isinstance(burning, bool):
            self.__burning = burning
        else:
            print "Error, incorrect burning!"
    burning = property(getBurning, setBurning)


    def getStick (self):
        return self.__stick

    def setStick (self, stick):
        if isinstance(stick, bool):
            self.__stick = stick
        else:
            print "Error, incorrect stick!"
    stick = property(getStick, setStick)


    def getStickType (self):
        return self.__stickType

    def setStickType (self, stickType):
        if isinstance(stickType, int) and (stickType == 0 or stickType == 1):
            self.__stickType = stickType
        else:
            print "Error, incorrect stickType!"
    stickType = property(getStickType, setStickType)


    def getWalk (self):
        return self.__walk

    def setWalk (self, walk):
        if isinstance(walk, int) and walk >= 0:
            self.__walk = walk
        else:
            print "Error, incorrect walk!"
    walk = property(getWalk, setWalk)


    def getRun (self):
        return self.__run

    def setRun (self, run):
        if isinstance(run, int) and run >= 0:
            self.__run = run
        else:
            print "Error, incorrect run!"
    run = property(getRun, setRun)


    def getJump (self):
        return self.__jump

    def setJump (self, jump):
        if isinstance(jump, int) and jump >= 0:
            self.__jump = jump
        else:
            print "Error, incorrect jump!"
    jump = property(getJump, setJump)


    def getRadiatorsOn (self):
        return self.__radiatorsOn

    def setRadiatorsOn (self, radiatorsOn):
        if isinstance(radiatorsOn, int) and radiatorsOn >= 0:
            self.__radiatorsOn = radiatorsOn
        else:
            print "Error, incorrect radiatorsOn!"
    radiatorsOn = property(getRadiatorsOn, setRadiatorsOn)


    def getRadiatorsOff (self):
        return self.__radiatorsOff

    def setRadiatorsOff (self, radiatorsOff):
        if isinstance(radiatorsOff, int) and radiatorsOff >= 0:
            self.__radiatorsOff = radiatorsOff
        else:
            print "Error, incorrect radiatorsOff!"
    radiatorsOff = property(getRadiatorsOff, setRadiatorsOff)


    def getWounds (self):
        return self.__wounds

    def setWounds (self, wounds):
        if isinstance(wounds, int) and wounds >= 0:
            self.__wounds = wounds
        else:
            print "Error, incorrect wounds!"
    wounds = property(getWounds, setWounds)


    def getConscious (self):
        return self.__conscious

    def setConscious (self, conscious):
        if isinstance(conscious, bool):
            self.__conscious = conscious
        else:
            print "Error, incorrect conscious!"
    conscious = property(getConscious, setConscious)


    def getAmmunitionNumber (self):
        return self.__ammunitionNumber

    def setAmmunitionNumber (self, ammunitionNumber):
        if isinstance(ammunitionNumber, int) and ammunitionNumber >= 0:
            self.__ammunitionNumber = ammunitionNumber
        else:
            print "Error, incorrect ammunitionNumber!"
    ammunitionNumber = property(getAmmunitionNumber, setAmmunitionNumber)


   
