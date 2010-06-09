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

import MechFile
import DefMech
from math import *
import os

def str2bool(string):
    if string.strip().lower() in ('yes', '1', 'true', 'si'):
        return True
    elif string.strip().lower() in ('no', '0', 'false'):
        return False
    else:
        return "Error: Not boolean" 

class Attack :
    def __init__ (self, playerNumber, mechs, dmech, fichBoard, board) :
        self.__playerNumber = playerNumber #Numero de jugador 
        self.__mechs = mechs #Conjunto de mechs de la partida
        self.__dmech = dmech # Conjunto de defmechs
        self.__fichBoard = fichBoard
        self.__board = board
        self.__enemys = [] #Lista de enemigos
        self.__player = mechs.mechSet[playerNumber] #Mech actual
        self.__enemysAttack = [] #Lista de enemigos en linea de vision
        self.__finalWeapons = [] #Lista de armas usadas en el ataque con armas
        self.__stick = False #Indica si se cogi el garrote al final del ataque con armas
        self.__log = ""

        #Creamos una lista de enemigos y seleccionamos al jugador actual
        for i in range(mechs.mechNumber) :
            if i != playerNumber :
               self.__enemys.append(mechs.mechSet[i])
    
    def printLog (self) :
    	file = open("x50608460.log", "a")
    	file.write(self.__log)
    	file.close()
    
    def physicalAttack (self):
        f = "AccionJ" + str(self.__playerNumber)+".sbt"
        f = open(f, "w")
        choiseEnemy = None
        distance = 0
        enemy = None

        self.__log = self.__log + "FASE DE ATAQUE FISICO =====================>\n"

        #Creamos una lista de enemigos atacables
        for i in range(len(self.__enemys))  :
            attack = self.visionLine(self.__enemys[i])
            
            ensuelo = self.enemys[i].ground
            
            goodf = self.relative_position( (int(self.__player.getCell()[2:])-1, int(self.__player.getCell()[0:-2])-1 ) , (int(self.__enemys[i].getCell()[2:])-1, int(self.__enemys[i].getCell()[0:-2])-1))
            
            brazos = ( ((((self.__player.facingTorsoSide - 1)+3)%6) != (goodf)%6) and ( (((self.__player.facingTorsoSide - 1)+3)%6) != ((goodf-1)%6) ) and ( (((self.__player.facingTorsoSide - 1)+3)%6) != ((goodf+1)%6) ))
            
            piernas = ( ((((self.__player.facingSide - 1)+3)%6) != (goodf)%6) and ( (((self.__player.facingSide - 1)+3)%6) != ((goodf-1)%6) ) and ( (((self.__player.facingSide - 1)+3)%6) != ((goodf+1)%6) ))

            adyacentes = self.areAdjacent( (int(self.__player.getCell()[2:])-1, int(self.__player.getCell()[0:-2])-1 ) , (int(self.__enemys[i].getCell()[2:])-1, int(self.__enemys[i].getCell()[0:-2])-1 ))
            
            diflevel = abs(self.__board.map[int(self.__player.getCell()[2:])-1][int(self.__player.getCell()[0:-2])-1].getLevel() - self.__board.map[int(self.__enemys[i].getCell()[2:])-1][int(self.__enemys[i].getCell()[0:-2])-1].getLevel())
			
	    if attack == True and adyacentes == True and diflevel == 0 :
        	self.__enemysAttack.append(self.__enemys[i])
        
        if len(self.__enemysAttack) > 0 :
            choiseEnemy = int(self.enemyMoreNear(self.__enemysAttack, distance) )

            if self.__stick == True :
                f.write("1" + "\n")
                f.write("BIBD" + "\n")
                f.write("3000" + "\n")
                f.write(enemy.getCell()+"\n")
                f.write("Mech" + "\n")
                self.__log = self.__log + "Atacamos con el garrote al Mech posicionado en la casilla "+ enemy.getCell()+"\n"
                #si no tenemos garrote pegamos punetazos
            else :            
                #debemos estimar que ataques se realizaron en el turno de ataqueArmas para saber que extremidad se puede usar

                enemy = self.__enemysAttack[choiseEnemy]
                    
                #comprobamos que armas se pueden usar contra el enemigo elegido
                choiseWeapons = self.choiseWeapons(enemy)
                   
                        
                #eleccion temperatura       
                temp = self.choiseTemperature(enemy)                        
                #eleccion definitiva de las armas a lanzar
                self.__finalWeapons = self.shootWeapons(enemy, temp, choiseWeapons)
                    
                BI = False
                PI = False
                BD = False
                PD = False
                used = 0
                for i in range(len(self.__finalWeapons)):
                    #localizacion del arma
                    itemLocation = self.__finalWeapons[i].getItemLocation()
                    if itemLocation == 0 : BI = True
                    elif itemLocation == 2:PI = True
                    elif itemLocation == 3: PD = True
                    elif itemLocation == 5: BD = True
                                
                #No se pueden dar dos patadas en el mismo turno (pegaremos con la pierna derecha)
                if PI == False and PD == False : PD = True

                #numero de extremidades que se usaran para el ataque
                if BI == False : used = used + 1
                if PI == False : used = used + 1
                if BD == False : used = used + 1
                if PD == False : used = used + 1

                    
                f.write(str(used) + "\n")

                                       
                if BI == False and brazos == True and ensuelo == False:
                    f.write("BI" + "\n")
                    f.write("1000" + "\n")
                    f.write(enemy.getCell()+"\n")
                    f.write("Mech" + "\n")
                    self.__log = self.__log + "Atacamos con el puño izquierdo al Mech posicionado en la casilla "+ enemy.getCell()+"\n"


                if BD == False and  brazos == True and ensuelo == False:
                    f.write("BD" + "\n")
                    f.write("1000" + "\n")                        
                    f.write(enemy.getCell()+"\n")
                    f.write("Mech" + "\n")
                    self.__log = self.__log + "Atacamos con el puño derecho al Mech posicionado en la casilla "+ enemy.getCell()+"\n"
                            
                if PI == False and piernas == True:
                    f.write("PI" + "\n")
                    f.write("2000" + "\n")
                    f.write(enemy.getCell()+"\n")
                    f.write("Mech" + "\n")
                    self.__log = self.__log + "Atacamos con la pierna izquierda al Mech posicionado en la casilla "+ enemy.getCell()+"\n"
                            
                if PD == False and piernas == True:
                    f.write("PD" + "\n")
                    f.write("2000" + "\n")
                    f.write(enemy.getCell()+"\n")
                    f.write("Mech" + "\n")
                    self.__log = self.__log + "Atacamos con la pierna derecha al Mech posicionado en la casilla "+ enemy.getCell()+"\n"
                
                   

        
        #no se ataca
        else:
            self.__log = self.__log + "No realiza ningún ataque físico por que no se cumplen los requisitos óptimos para realizarlo\n"
            f.write("0"+"\n")
        
        f.close()
        self.__log = self.__log + "=============================>\n\n"
        
     
    def weaponsAttack (self):
        attack = False
        choiseEnemy = None
        distance = None
        finalChoise = None
        choiseWeapons = None
        temp = 0
        f = "AccionJ" + str(self.__playerNumber)+".sbt"
        
        self.__log = self.__log + "FASE DE ATAQUE CON ARMAS =====================>\n"
    
        
        #Creamos una lista de enemigos atacables
        for i in range(len(self.__enemys))  :
            attack = self.visionLine(self.__enemys[i])
            
            goodf = self.relative_position( (int(self.__player.getCell()[2:])-1, int(self.__player.getCell()[0:-2]) -1) , (int(self.__enemys[i].getCell()[2:])-1, int(self.__enemys[i].getCell()[0:-2])-1))
			
	    if attack == True and ( ((((self.__player.facingTorsoSide - 1)+3)%6) != (goodf)%6) and ( (((self.__player.facingTorsoSide - 1)+3)%6) != ((goodf-1)%6) ) and ( (((self.__player.facingTorsoSide - 1)+3)%6) != ((goodf+1)%6) ) ) : 
                self.__enemysAttack.append(self.__enemys[i])

        
        #Se puede atacar ?
        if len(self.__enemysAttack) > 0 :
            #seleccionamos el enemigo a atacar(mas cercano)
            choiseEnemy = int(self.enemyMoreNear(self.__enemysAttack, distance) )
            
            #comprobamos que armas se pueden usar contra el enemigo elegido
            choiseWeapons = self.choiseWeapons(self.__enemysAttack[choiseEnemy])
            
            #eleccion temperatura
            temp = self.choiseTemperature(self.__enemysAttack[choiseEnemy])
            
            #eleccion definitiva de las armas a lanzar
            self.__finalWeapons = self.shootWeapons(self.__enemysAttack[choiseEnemy], temp, choiseWeapons)
            
            #Escribimos el ataque que vamos a realizar en el fichero de AccionJ
            self.writeWeaponsAttack(self.__finalWeapons, self.__enemysAttack[choiseEnemy], f)
        
        #si no se puede atacar lo escribimos en el fichero de AccionJ
        elif len(self.__enemysAttack) == 0 :
            self.__log = self.__log + "No se realiza ningún ataque con armas debido a que no se cumplen las condiciones óptimas para realizarlo\n"
            self.writeNoAttack(self.__enemysAttack, f)
        
        self.__log = self.__log + "=============================>n\n"
            
        
    
    def writeNoAttack(self, Enemys, f):
        f = open (f, "w")
        distance = None
        
        #comprobamos si hay un garrote en la casilla del jugador
        if self.__board.map[int(self.__player.getCell()[2:])-1][int(self.__player.getCell()[0:-2])-1] == True :   
            #buscamos el enemigo mas cercano
            choiseEnemy = int(self.enemyMoreNear(Enemys, distance))
            
            #Si esta la distancia es menor o igual a 4 cogeremos el garrote
            if distance <= 4 :
                f.write("True" + "\n")
                self.__stick = True 
                self.__log = self.__log + "Recogemos un garrote de la casilla "+ self.__player.getCell()+"\n"
            else :
                f.write("False" + "\n")
                f.write("0000" + "\n")
                f.write("0" + "\n")
        else: 
            f.write("False" + "\n")
            f.write("0000" + "\n")
            f.write("0" + "\n")
        
        f.close()
            
            
    def writeWeaponsAttack(self, finalWeapons, Enemy, f):
        f = open (f, "w")
        
        if len(finalWeapons) == 0:
            f.write ("False" +"\n")
            f.write ("0000" +"\n")
            f.write ("0" +"\n")
            self.__log = self.__log + "No se realiza ningún ataque con armas debido a que no se cumplen las condiciones óptimas para realizarlo\n"
        else :
            #No cogemos el garrote
            f.write("False"+ "\n")
            #Hexagono objetivo primario
            f.write(Enemy.getCell()+"\n")
        
            #numero de armas
            f.write(str(len(finalWeapons))+"\n")
            
            #por cada arma
            numComponents = self.__dmech[self.__playerNumber].mech.getEquippedComponentsNumber() 
            numActuators = self.__dmech[self.__playerNumber].mech.getActuatorsNumber()

            for i in range(len(finalWeapons)):    
                #localizacion del arma
                itemLocation = finalWeapons[i].getItemLocation()
                if itemLocation == 0 : f.write("BI"+"\n")
                elif itemLocation == 1: f.write("TI"+"\n")
                elif itemLocation == 2: f.write("PI"+"\n")
                elif itemLocation == 3: f.write("PD"+"\n") 
                elif itemLocation == 4: f.write("TD"+"\n")
                elif itemLocation == 5: f.write("BD"+"\n")
                elif itemLocation == 6: f.write("TC"+"\n")
                elif itemLocation == 7: f.write("CAB"+"\n")
                
                #numero de slot donde esta el arma
                loca = self.__dmech[self.__playerNumber].mech.location[itemLocation]
                encontrado = False
                j = 0
                while j < loca.getSlotNumber() and not(encontrado):
                    if loca.slot[j].getCode() == finalWeapons[i].getCode():
                        encontrado = True
                        f.write(str(j)+"\n")
                    j = j + 1

                
                
                #Disparo a doble cadencia -> siempre false, no es buena estrategia
                f.write("False"+"\n")

                #Arma tipo energia?
                if finalWeapons[i].getWeaponType()[0:5] == "Energ":
                    f.write("-1"+"\n")
                    f.write("-1"+"\n")
                #si no es de energia buscamos donde esta la municion
                else:
                    k = 0
                    encontrado1 = False
                    while k < numComponents and not(encontrado1):
                        if self.__dmech[self.__playerNumber].mech.component[k].getWeaponCode() == finalWeapons[i].getCode() :
                            ammunitionCode = self.__dmech[self.__playerNumber].mech.component[k].getCode()
                            encontrado1 = True
                            h = 0
                            encontrado2 = False
        
                            while h < numComponents and not(encontrado2):
                                if self.__dmech[self.__playerNumber].mech.component[h].getCode() == ammunitionCode:
                                    encontrado2 = True
                                    itemLocation = self.__dmech[self.__playerNumber].mech.component[h].getItemLocation()
                                    if itemLocation == 0 : f.write("BI"+"\n")
                                    elif itemLocation == 1: f.write("TI"+"\n")
                                    elif itemLocation == 2: f.write("PI"+"\n")
                                    elif itemLocation == 3: f.write("PD"+"\n") 
                                    elif itemLocation == 4: f.write("TD"+"\n")
                                    elif itemLocation == 5: f.write("BD"+"\n")
                                    elif itemLocation == 6: f.write("TC"+"\n")
                                    elif itemLocation == 7: f.write("CAB"+"\n")
                        
                                    #numero de slot donde esta la municion
                                    loca = self.__dmech[self.__playerNumber].mech.location[itemLocation]
                                    encontrado3 = False
                                    j = 0
                                    while j < loca.getSlotNumber() and not(encontrado3):
                                        if loca.slot[j].getCode() == ammunitionCode :
                                            encontrado3 = True
                                            f.write(str(j)+"\n")
                                        j = j +1
								h = h +1
						k = k + 1

                #Hexagono objetivo del arma
                f.write(Enemy.getCell()+"\n")
                f.write("Mech"+"\n")
                
                self.__log = self.__log + "Disparamos el arma "+ finalWeapons[i].getName() +" al enemigo posicionado en la casilla "+Enemy.getCell()+"\n"

        
        f.close()
                                
    
    def shootWeapons(self, Enemy, temp, choiseWeapons) :
        cumulativeTemp = 0
        #ordenamos las armas lanzables por calidad
        for i in range(len(choiseWeapons)):        
            """Ordena la lista por el metodo burbuja mejorado y 
         ademas sale del ciclo de pasadas, en cuanto detecta 
         que al final de una pasada no se realizaron 
         intercambios.""" 
            intercambios=1 
            pasada=1 
            while pasada<len(choiseWeapons) and intercambios==1 : 
                intercambios=0 
                for i in range(0,len(choiseWeapons)-pasada):  
                    if (choiseWeapons[i].getHarm()/choiseWeapons[i].getHeat()) >  (choiseWeapons[i+1].getHarm()/choiseWeapons[i+1].getHeat()): 
                        choiseWeapons[i], choiseWeapons[i+1] = choiseWeapons[i+1], choiseWeapons[i] 
                        intercambios=1  
                    pasada += 1 
        #compruebo cuantas armas de las seleccionadas puedo disparar sin superar el limite de calor    
        finalWeapons = []
        numWeapons = 0
        for i in range(len(choiseWeapons)):
            if not(cumulativeTemp + choiseWeapons[i].getHeat() > temp):
                cumulativeTemp = cumulativeTemp + choiseWeapons[i].getHeat()
                finalWeapons.append(choiseWeapons[i])
        return finalWeapons
        
       
            
    def choiseTemperature(self, Enemy):
        tempPlayer = self.__player.getTemp()
        if tempPlayer < 10 : temp = 12
        elif (tempPlayer >= 10 and tempPlayer < 15) : temp = 9
        elif (tempPlayer >= 15 and tempPlayer < 20) : temp = 6
        elif (tempPlayer >= 20 and tempPlayer < 26) : temp = 4
        elif (tempPlayer >= 26) : temp = 2
        
        if Enemy.getWounds() <= 40 : WeakEnemy = True
        if self.__player.getWounds() <= 40 : WeakPlayer = True
        
        if WeakPlayer and WeakEnemy : temp = temp * 1.5
        if WeakPlayer and (not(WeakEnemy)) : temp = temp * 1.25
        if not(WeakPlayer) and WeakEnemy : temp = temp * 1.25
        
        return temp
        
    
    def choiseWeapons(self, Enemy):
        disWeapons = []
        for  i in range(self.__dmech[self.__playerNumber].mech.getEquippedComponentsNumber() ):
            if self.__dmech[self.__playerNumber].mech.component[i].getType() == "ARMA":
                distance = self.dist2((int(self.__player.getCell()[0:-2])-1, int(self.__player.getCell()[2:])-1 ) , (int(Enemy.getCell()[0:-2])-1, int(Enemy.getCell()[2:])-1))
                if (distance <= self.__dmech[self.__playerNumber].mech.component[i].longDistance) and self.__dmech[self.__playerNumber].mech.component[i].operativeTeam :
                    disWeapons.append(self.__dmech[self.__playerNumber].mech.component[i])
        return disWeapons
                                           
    
    def enemyMoreNear(self, enemysList, distance):
        i = 1
        min = 0
        distance = self.dist2((int(self.__player.getCell()[0:-2])-1, int(self.__player.getCell()[2:])-1) , (int(enemysList[0].getCell()[0:-2])-1, int(enemysList[0].getCell()[2:])-1))
       
        while i < len(enemysList):
            if (distance >  self.dist2((int(self.__player.getCell()[0:-2])-1, int(self.__player.getCell()[2:])-1 ) , (int(enemysList[i].getCell()[0:-2])-1, int(enemysList[i].getCell()[2:])-1 )) ):    
                distance = self.dist2((int(self.__player.getCell()[0:-2])-1, int(self.__player.getCell()[2:])-1 ) , (int(enemysList[i].getCell()[0:-2])-1, int(enemysList[i].getCell()[2:])-1)) 
                min = i
            i = i +1
        return min

    def euclideanDis(self, c1, c2):
        return sqrt(((int(c2[0:2])-int(c1[0:2]))*(int(c2[0:2])-int(c1[0:2])))+((int(c2[2:4])-int(c1[2:4]))*(int(c2[2:4])-int(c1[2:4]))))             

    def visionLine(self, enemy):
        if self.__player.getGround() == True :
            GroundPlayer = "1"
        else: 
            GroundPlayer = "0"
        
        if self.__mechs.mechSet[enemy.getPlayerNumber()].getGround() == True :
            GroundEnemy = "1"
        else:
            GroundEnemy = "0"
        
        cellGoal = self.__mechs.mechSet[enemy.getPlayerNumber()].getCell()
        cellSource = self.__player.getCell()
        
        execute = "LDVyC.exe "+self.__fichBoard+" "+cellSource+" "+GroundPlayer+" "+cellGoal+" "+GroundEnemy
        
        #ejecutar el programa de LineaVison
        os.system(execute)
        
        try:
            file = open("LDV.sbt", "r")
        except IOError:
            print "The file LDV.sbt  does not exist"
            return -1
        
        file.readline(); 
        isVisionLine = str2bool ( file.readline() )
        file.close()
        return isVisionLine

    def areAdjacent(self, c, c2):       
        slist=[]
        for i in (-1,0,1):
            for j in (-1,0,1):
                if ((c[1]+1)%2 == 0): #columnas pares
                    if (i == -1 and j == -1) or (i == 0 and j == 0) or (i == 1 and j == -1):
                        continue
                else:
                    if (i == 1 and j == 1) or (i == 0 and j == 0) or (j == 1 and i == -1):
                            continue
                newFil = (c[0]) +j
                newCol = (c[1]) +i

                slist.append((newFil, newCol))
        return c2 in slist

    def dist2 (self, c1,c2):
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

    def relative_position(self, c1, c2):
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

