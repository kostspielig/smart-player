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
        self.player = playerN
        self.board = board
        self.mechs = mechs
        self.ini = ini
        self.movType = None
        self.nextCell = None
        self.nextFace = None
        self.masc = None
        self.stepNumber = None
        self.step = []

    def findNextPosition(self):
        return 0

    def setTarjet(self):
        """ Finds out the player we are going to approach
            returns the player number
        """
        t = 0
        tarjet = sys.maxint
        for m in self.mechs.mechSet:
            if m.playerNumber == self.player:
                continue
            d = dist((self.mechs.mechSet[self.plater].cell[0:-2],
                  self.mechs.mechSet[self.plater].cell[2:]),(m.cell[0:-2], m.cell[2:]))
            if d < tarjet:
                t = m.playerNumber
        return t

    def printAccion(self):

        file = open("accionJ"+ str(self.player)+".sbt", "w")
                    
        file.write(str(self.movType) +"\n")

     
        file.close()

def str2bool(string):
    return string.strip().lower() in ('yes', '1', 'true')

def dist (c1,c2):
        return abs(c2[0]-c1[0]) + abs(c2[1]-c1[1])
