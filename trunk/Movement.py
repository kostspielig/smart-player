#!/usr/bin/python

__id__ = "$Id: Movement.py $"
__version__ = "$Revision: 8 $"
__date__ = "$Date: 06/06/2010 Sat  $"
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
        self.playerFace = self.player.facingSide -1
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
            if d < distance:
                t = m.playerNumber
                distance = d
        return t, distance

    def nextMove(self):
        enemy,distance = self.setTarjet()
        faceTorsoEnemy = (self.mechs.mechSet[enemy].facingSide+2 )%6 #[0-5]

        enemyCell = int(self.mechs.mechSet[enemy].cell[2:])-1,int(self.mechs.mechSet[enemy].cell[0:-2])-1
 
        # Si estamos en el suelo -> Nos levantamos
        if self.player.ground == True and self.player.walk >= 2:
            self.getUp = True
            face = relative_position(self.playerCell, enemyCell)
            self.movType = 0 # We try to get up by walking
            self.nextCell = self.playerCell
            self.nextFace = face
            self.stepCell.append((4,face)) #Levantarse , face

        # If we do move first -> Hide
        elif self.ini.position.index(self.playerN)< self.ini.position.index(enemy):
            print "Hidding"
            self.path, self.movType = self._hide(enemyCell, distance)
            print self.path
        else: #We do move last -> go for the enemy's back!
            print "Approaching"
            self.path, self.movType = self._approach( enemyCell,faceTorsoEnemy )
            print self.path

        self.printAction()
        self.printLog()

        
    def _hide (self, enemy, distance2enemy):
        path = []
        pos, face = self.posible_positions(enemy, distance2enemy)
        # Si no ai posiciones cercanas cambiamos nuestro encaramiento
        if pos == []: 
            face = relative_position(self.player, enemy)
            if face != self.playerFace: 
                pos.append(self.playerCell)
        pf = pathfinder.PathFinder(self.board.successors, self.board.move_cost, self.board.heuristic_to_goal)
        A = Pos(self.playerCell, self.playerFace)
        for x in pos:
            face = relative_position (x, enemy)
            B = Pos(x, face)
            path, can, cost = pf.compute_path_until_PM (A, B, 0, self.player.walk)

            if can == True: return (path,0)
            if can == False and self.player.run != 0:
                path2, can2, cost2 = pf.compute_path_until_PM(A, B, 1, self.player.run)
                if can2 == True:
                    return (path2, 1)
            if can == False and self.player.jump != 0:
                path3, can3, cost3 = pf.compute_path_until_PM(A, B, 2, self.player.jump)
                if can3 == True:
                    return (path3,2)
        return (path, 0)

    def posible_positions (self,enemyCell, distance2enemy):
        positions = []
        faceEnemy = relative_position (self.playerCell, enemyCell)
        face = faceEnemy
        #if distance2enemy <3:
        #    face = (face+3)%6
        cell = self.playerCell
        newCell = cell
        for i in range(2):
            cell = newCell
            for j in [0,1,-1]:
                newCell = Board.adjacent_cells(cell, face+j, self.board)
                if newCell == 0: continue
                # Miramos si ai algun bosque denso o  ligero
                obj = self.board.map[newCell[0]][newCell[1]].objects
                if obj == 1 or obj == 2:
                    positions.append(newCell)

        return positions, faceEnemy
    

    def _approach (self, enemy, faceTorsoEnemy):
        i = 0
        x = 0
        while True:
            x = Board.adjacent_cells(enemy, (faceTorsoEnemy+i)%6, self.board)
            i += 1
            if (not x in self.mechs.enemys_cell()) and x != 0: break
        pf = pathfinder.PathFinder(self.board.successors, self.board.move_cost, self.board.heuristic_to_goal)
        A = Pos(self.playerCell, self.playerFace)
        B = Pos(x, Board.facing_side(x, enemy))
        if A == B: return ([], 3)

        path, can, cost = pf.compute_path_until_PM (A, B, 0, self.player.walk)

        if can == False and self.player.run != 0:
            path2, can2, cost2 = pf.compute_path_until_PM(A, B, 1, self.player.run)

            if can2 == True:
                return (path2, 1)
        if can == False and self.player.jump != 0:
            print "ESTO K ES!: walk then jump"
            print self.player.walk
            print self.player.jump
            path3, can3, cost3 = pf.compute_path_until_PM(A, B, 2, self.player.jump)
            if (can3 == True) or  (self.player.jump >= self.player.walk):
                return (path3,2)
        return (path, 0)

    def printAction(self):

        file = open("accionJ"+ str(self.playerN)+".sbt", "w")
        if self.path == []: self.movType =3
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
            
        elif (self.movType == 0 or self.movType == 1) and self.path != []: # Andar o correr
            p = self.path[len(self.path)-1]
            print p
            file.write(str(p.printPos()) +"\n") #Hex destino
            file.write(str(p.printFace()) +"\n") #Lado hex destino
            file.write(str(self.masc) +"\n") #Usar masc? 
            move,s = self.calculate_steps()
            file.write(str(s) +"\n") #Numero de pasos
            for x in move:
                file.write(str(step[x[0]]) +"\n")
                file.write(str(x[1]) +"\n")
            ret = 0
        elif self.movType == 2: # Saltar
            p = self.path[len(self.path)-1]
            file.write(str(p.printPos()) +"\n")
            file.write(str(p.printFace()) +"\n")
            ret = 2
        elif self.movType == 3 or self.path == []: # Inmovil -> Do Nothing
            ret = 3

        file.close()
        return ret

    def printLog(self):
        file = open("x50608460.log", "a")
        file.write (" FASE DE MOVIMIENTO ====================>\n")
        file.write ("Tipo de movimiento :  " +str(mov[self.movType])+ "\n")
        file.write (" ___Camino___ \n")
        file.write (str(self.path) + " \n")
        file.write ("<========================================\n\n")
        file.close ()
        

    def calculate_steps(self):
        #y = self.path[0]
        #for x in self.path[1:]:
        moves = []
        s = 0
        i = 1
        while i < len(self.path): 
            y = self.path[i-1] 
            x = self.path[i]
            if y.face != x.face:
                costFace = min( (x.face - y.face)%6, (y.face - x.face)%6 )
                if (y.face - costFace) % 6 == x.face:
                    moves.append((2,costFace))
                    s += 1
                    if i+1 !=len(self.path) or x.pos != y.pos: 
                        moves.append((0,1))
                        s+= 1
                else: 
                    moves.append((3, costFace))
                    s += 1
                    if i+1 !=len(self.path) or x.pos != y.pos: 
                        moves.append((0,1))
                        s+= 1
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
                moves.append((0, aux))
                s+= 1
        return moves,s

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
        if (c1[1]+1)%2 == 0: #columnas pares
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
