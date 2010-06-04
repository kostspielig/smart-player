#!/usr/bin/python

__id__ = "$Id: Movement.py $"
__version__ = "$Revision: 1 $"
__date__ = "$Date: 20/04/2010 Sat  $"
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

import sys
import pathfinder
import Board
import MechFile
import Initiative

class Movement:
    
    def __init__ (self, playerN, board, mechs, ini):
        self.player = playerN # Number of current player
        self.board = board    # Map
        self.mechs = mechs    # Info about opponent mechs
        self.ini = ini        # Initiative file
        self.movType = None
        self.nextCell = None
        self.nextFace = None
        self.masc = False     # By convention is set to False
        self.stepNumber = None
        self.step = [] # (stepType, times/face)
                       # stepType 1 - adelante 2 - atras 3 - izquierda 4 - derecha 5 -levantarse 6 - cuerpo a tierra

    def findNextPosition(self):
        return 0

    def setTarjet(self):
        """ Finds out the player we are going to approach
            returns the player number
        """
        t = 0
        distance = sys.maxint
        for m in self.mechs.mechSet:
            if m.playerNumber == self.player:
                continue
            d = dist2((int(self.mechs.mechSet[self.player].cell[0:-2]),
                  int(self.mechs.mechSet[self.player].cell[2:])),(int(m.cell[0:-2]),int( m.cell[2:])))
            print "distance to " + str(m.playerNumber) + "equals to " +str(d)
            if d < distance:
                t = m.playerNumber
                distance = d
        return t

    def nextMove(self):
        enemy = self.setTarjet()
        if self.mechs[self.player].ground == True:
            self.movType = 0 # We try to get up by walking
            self.step.append(())

    def printAccion(self):

        file = open("accionJ"+ str(self.player)+".sbt", "w")
                    
        file.write(str(self.movType) +"\n")

     
        file.close()

def str2bool(string):
    return string.strip().lower() in ('yes', '1', 'true')

def dist (c1,c2):
    """ Manhatan distance
    """
    return abs(c2[0]-c1[0]) + abs(c2[1]-c1[1])

def dist2 (c1,c2):
    """ Exact distance
    """
    Vx = abs(c2[0]-c1[0])
    Vy = abs(c2[1]-c1[1])
    if Vy%2 != 0:
        factor = 0
    elif c1[1] < c2[1]: 
        factor = (c1[0]-1)%2
    else:
        factor = (c2[0]-1)%2

    return Vx + max(0, Vy- (Vx/2) - factor)

if __name__ == "__main__": 

    actualPlayer = 4

    # Reading the board
    board = Board.Board()
    board.readBoard("../ficheros/mapaJ"+str(actualPlayer)+".sbt")

    # Reading the mech file
    mechs = MechFile.MechFile()
    mechs.readMechFile("../ficheros/mechsJ"+str(actualPlayer)+".sbt")

    # Reading initiative file
    ini = Initiative.Initiative()
    ini.readInitiative("../ficheros/iniciativaJ"+str(actualPlayer)+".sbt")

    strategy = Movement(actualPlayer, board, mechs, ini)

    print strategy.setTarjet()
