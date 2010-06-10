#!/usr/bin/python

__id__ = "$Id: Reaction.py $"
__version__ = "$Revision: 2 $"
__date__ = "$Date: 07/06/2010 Sat  $"
__author__ = "Maria Carrasco Rodriguez, Francisco Manuel Herrero Perez"
__license__ = "GPL"
__URL__ = "http://code.google.com/p/smart-player/"

import sys
import Movement

change = {0: 'Igual', 1: 'Derecha', 2: 'Izquierda'}

class Reaction:
    """ Reaction Phase """

    def __init__ (self, actualPlayer, board, mechs, ini ):
        self.playerN = actualPlayer
        self.board = board
        self.mechs = mechs
        self.ini = ini
        self.player = self.mechs.mechSet[self.playerN]
        self.playerCell = ( int(self.player.cell[2:] ) -1, 
                            int(self.player.cell[0:-2] )-1 )
        self.playerFace = self.player.facingSide -1
        self.newFace = change[0]

    def calculate_reaction(self):
        enemy,distance = self.setTarjet()
        faceTorsoEnemy = (self.mechs.mechSet[enemy].facingSide+2 )%6 #[0-5]
        enemyCell = (int(self.mechs.mechSet[enemy].cell[2:])-1, 
                     int(self.mechs.mechSet[enemy].cell[0:-2])-1)
        facePos = Movement.relative_position(self.playerCell, enemyCell)
        if self.playerFace != facePos:
            if ( (self.playerFace +1)%6 == facePos ) or ((self.playerFace +2)%6 == facePos):
                self.newFace = change[1]
            elif ( (self.playerFace -1)%6 == facePos) or ((self.playerFace -2)%6 == facePos):
                self.newFace = change[2]

        self.printAction()
        self.printLog()

    def printAction(self):
        file = open("accionJ"+ str(self.playerN)+".sbt", "w")
        
        file.write(str(self.newFace) +"\n")

        file.close()

    def printLog(self):
        file = open("x50608460.log", "a")
        file.write (" FASE DE REACCION =====================>\n")
        if self.newFace != change[0]: # Si no nos quedamos quietos
            file.write ("Cambiamos el encaramiento moviendonos hacia la "+ self.newFace + "\n")
        else:
            file.write ("Nos quedamos con el mismo encaramiento \n")
        file.write ("<=======================================\n\n")
        file.close ()


    def setTarjet(self):
        """ Finds out the player we are going to approach
        returns the enemy number + distance to enemy
        """
        t = 0
        distance = sys.maxint
        for m in self.mechs.mechSet:
            if m.playerNumber == self.playerN:
                continue
            d = Movement.dist2((int(self.player.cell[0:-2]),
                       int(self.player.cell[2:])),(int(m.cell[0:-2]),int( m.cell[2:])))
            print "distance to " + str(m.playerNumber) + "equals to " +str(d)
            if d < distance:
                t = m.playerNumber
                distance = d
        return t, distance
