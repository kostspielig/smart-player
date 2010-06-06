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
from pathfinder import Pos


mov = {0: 'Andar', 1: 'Correr', 2: 'Saltar', 3: 'Inmovil'}
step = {0: 'Adelante', 1: 'Atras', 2: 'Izquierda', 3: 'Derecha', 4: 'Levantarse', 5: 'Cuerpo a Tierra'}

class Movement:


    def __init__ (self, playerN, board, mechs, ini):
        self.playerN = playerN # Number of current player
        self.board = board    # Map
        self.mechs = mechs    # Info about opponent mechs
        self.ini = ini        # Initiative file
        self.movType = None
        self.nextCell = None
        self.nextFace = None
        self.masc = False     # By convention is set to False
        self.stepNumber = None
        self.stepCell = [] # (stepType, times/face)
        # stepType: 1-adelante 2-atras 3-izquierda
        # 4-derecha 5-levantarse 6-cuerpo a tierra
        self.path = None
        self.player = self.mechs.mechSet[self.playerN]
        self.playerCell = int(self.player.cell[2:] ) -1, int(self.player.cell[0:-2] )-1
        self.playerFace = self.player.facingSide
        self.getUp = False

    def findNextPosition(self):
        return 0

    def setTarjet(self):
        """ Finds out the player we are going to approach
        returns the enemy number + distance to enemy
        """
        t = 0
        distance = sys.maxint
        for m in self.mechs.mechSet:
            if m.playerNumber == self.playerN:
                continue
            d = dist2((int(self.player.cell[0:-2]),
                       int(self.player.cell[2:])),(int(m.cell[0:-2]),int( m.cell[2:])))
            print "distance to " + str(m.playerNumber) + "equals to " +str(d)
            if d < distance:
                t = m.playerNumber
                distance = d
        return t, distance

    def nextMove(self):
        print "walk: "+str(self.player.walk)
        print "run: "+str(self.player.run)
        print "jump: "+str(self.player.jump)
        enemy,distance = self.setTarjet()
        faceTorsoEnemy = self.mechs.mechSet[enemy].facingTorsoSide
        cellEnemy = int(self.mechs.mechSet[enemy].cell[2:])-1,int(self.mechs.mechSet[enemy].cell[0:-2])-1
 
        # Si estamos en el suelo -> Nos levantamos
        if self.player.ground == True and self.player.walk >= 2:
            self.getUp = True
            face = relative_position(self.playerCell, cellEnemy)
            self.movType = 0 # We try to get up by walking
            self.nextCell = self.playerCell
            self.nextFace = face
            self.stepCell.append((4,face)) #Levantarse , face

        # If we do move first -> Hide
        if self.ini.position.index(self.playerN)< self.ini.position.index(enemy):
            print self.ini.position
            self._hide(cellEnemy)
        else: #We do move last -> go for the enemy's back!
            print "Moving last"
            self.path, cost, self.movType = self._approach( cellEnemy,faceTorsoEnemy )

        self.printAction()

        
    def _hide (self, enemy):
        self.movType = 3
    

    def _approach (self, enemy, faceTorsoEnemy):

        x = Board.adjacent_cells(enemy, faceTorsoEnemy)    
        pf = pathfinder.PathFinder(self.board.successors, self.board.move_cost, self.board.heuristic_to_goal)
        A = Pos(self.playerCell, self.playerFace)
        B = Pos(x, faceTorsoEnemy)
        path, can, cost = pf.compute_path_until_PM (A, B, 0, self.player.walk)
        if can == False and self.player.run != 0:
            path2, can2, cost2 = pf.compute_path_until_PM(A, B, 1, self.player.run)
            if can2 == True:
                return path2, cost2, 1
        if can2 == False and self.player.jump != 0:
            path3, can3, cost3 = pf.compute_path_until_PM(A, B, 2, self.player.jump)
            if can3 == True:
                return path3,cost3,2
        return path, cost, 0

    def printAction(self):

        file = open("accionJ"+ str(self.playerN)+".sbt", "w")
        
        file.write(str(mov[self.movType]) +"\n")
        if self.getUp == True:
            p = Pos(self.nextCell, self.nextFace)
            file.write(str(p.printPos()) +"\n") #Hex destino
            file.write(str(p.printFace()) +"\n") #Lado hex destino
            file.write(str(self.masc) +"\n") #Usar masc? 
            file.write(str(1) +"\n")
            file.write(str(step[4]) +"\n")
            file.write(str(p.printFace()) +"\n")
            ret = 0
            
        elif self.movType == 0 or self.movType == 1: # Andar o correr
            p = self.path[len(self.path)-1]
            file.write(str(p.printPos()) +"\n") #Hex destino
            file.write(str(p.printFace()) +"\n") #Lado hex destino
            file.write(str(self.masc) +"\n") #Usar masc? 
            move = self.calculate_steps()
            for x in move:
                file.write(str(step[x[0]]) +"\n")
                file.write(str(x[1]) +"\n")
            ret = 0
        elif self.movType == 2: # Saltar
            p = self.path[len(self.path)-1]
            file.write(str(p.printPos()) +"\n")
            file.write(str(p.printFace()) +"\n")
            ret = 2
        elif self.movType == 3: # Inmovil -> Do Nothing
            ret = 3

        file.close()
        return ret

    def calculate_steps(self):
        #y = self.path[0]
        #for x in self.path[1:]:
        moves = []
        i = 1
        while i < len(self.path): 
            y = self.path[i-1]; x = self.path[i]
            if y.face != x.face:
                costFace = min( (x.face - y.face)%6, (y.face - x.face)%6 )
                if (y.face - costFace) % 6 == x.face:
                    moves.append((2,costFace))
                else: moves.append((3, costFace))
                i += 1
            else:
                aux = 1
                i += 1
                while i < len(self.path):
                    y = self.path[i-1]; x = self.path[i]
                    if x.face == y.face:
                        aux += 1
                    else: break
                    i += 1
                moves.append(0, aux)
        return moves

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

def relative_position(c1, c2):
    if c1[0] > c2[0]: # Fila Norte
        if c1[1] == c2[1]: # same col
            return 0
        if c1[1] > c2[1]: # col
            return 5
        if c1[1] < c2[1]: #  col
            return 1
    elif c1[0] < c2[0]: # Fila sur
        if c1[1] == c2[1]:
            return 3
        if c1[1] > c2[1]:
            return 4
        if c1[1] < c2[1]:
            return 2
    else: # c1[0] == c2[0] # misma fila
        if c1[1]+1%2 == 0: #columnas pares
            if c1[1] > c2[1]:
                return 5
            else: #c1[1] < c2[1]
                return 1
        else: # columnas impares
            if c1[1] > c2[1]:
                return 4
            else: #c1[1] < c2[1]
                return 2

def calculate_steps( path):
    #y = self.path[0]
    #for x in self.path[1:]:
    moves = []
    i = 1
    while i < len(path): 
        y = path[i-1]; x = path[i]
        if y.face != x.face:
            costFace = min( (x.face - y.face)%6, (y.face - x.face)%6 )
            if (y.face - costFace) % 6 == x.face:
                moves.append((step[2],costFace))
            else: moves.append((step[3], costFace))
            i += 1
        else:
            aux = 1
            i += 1
            while i < len(path):
                y = path[i-1]; x = path[i]
                if x.face == y.face:
                    aux += 1
                else: break
                i += 1
            moves.append((step[0], aux))
    return moves


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

    strategy.nextMove()
