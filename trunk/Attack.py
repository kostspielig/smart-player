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
import Board
import os

class Attack:

    def __init__ (self, playerNumber, mechs, fichBoard, dmech, board ):
        self.__playerNumber = playerNumber
        self.__mechs = mechs
        self.__fichBoard = fichBoard
        self.__board = board
        self.__dmech = dmech
        self.__enemys = None
        self.__player = None
        
        #buscamos aljugador actual
        for i in range(self.__mechs.mechNumber) :
            if self.__mechs.mechSet[i].getPlayerNumber == self.__playerNumber :
                self.__player = self.__mechs.mechSet[i]
        
        #Creamos una lista de enemigos
        for i in range(self.__mechs.mechNumber) :
            if (self.__playerNumber != self.__mechs.mechSet[i].getPlayerNumber):
                self.__enemys.append(self.__mechs.mechSet[i])
       
    def weaponsAttack (self):
        enemysAttack = None
        attack = False
        choiseEnemy = None
        distance = None
        finalChoise = None
        choiseWeapons = None
        temp = 0
        f = "AccionJ" + str(self.__playerNumber)+".sbt"
        
        
        #Creamos una lista de enemigos atacables
        for i in range(self.__enemys)  :
            attack = self.visionLine(self.__enemys)
            if attack == True :
                enemysAttack.append(self.__enemys[i])
        
        #Se puede atacar ?
        if enemysAttack != None :
            #seleccionamos el enemigo a atacar(m�s cercano)
            choiseEnemy = int(self.enemyMoreNear(enemysAttack, distance) )
            
            #comprobamos que armas se pueden usar contra el enemigo elegido
        
            choiseWeapons = self.choiseWeapons(self.__enemys[choiseEnemy])
            
            #eleccion temperatura
          
            temp = self.choiseTemperature(self.__enemys[choiseEnemy])
            
            #eleccion definitiva de las armas a lanzar
            
            finalWeapons = self.shootWeapons(self.__enemys[choiseEnemy], temp, choiseWeapons)
            
            self.writeDistanceAttack(finalWeapons, self.__enemys[choiseEnemy], f)
        
        #si no se puede atacar
        else :
            self.writeNoAttack(self.__enemys, f)
    
    def writeNoAttack(self, Enemys, f):
        f = open (f, "w")
        distance = None
        
        #comprobamos si hay un garrote en la casilla del jugador
        if self.__player.getCell().getStick() == True :    
            #buscamos
            choiseEnemy = int(self.enemyMoreNear(Enemys, distance))
            
            #Si est� la distancia es menor o igual a 4 cogeremos el garrote
            if distance <= 4 :
                f.write("True" + "\n")
            else :
                f.write("False" + "\n")
                f.write("0000" + "\n")
                f.write("0" + "\n")
        else: 
            f.write("False" + "\n")
            f.write("0000" + "\n")
            f.write("0" + "\n")
        
        f.close()
            
            
             
            
    def writeDistanceAttack(self, finalWeapons, Enemy, f):
        f = open (f, "w")
        
        if len(finalWeapons) == 0:
            f.write ("False" +"\n")
            f.write ("0000" +"\n")
            f.write ("0" +"\n")
        else :
            #No cogemos el garrote
            f.write("False"+ "\n")
            #Hexagono objetivo primario
            if Enemy.getCell().getX() < 10 and Enemy.getCell.getY() < 10 :
                f.write("0"+str(Enemy.getCell().getX())+"0"+str(Enemy.getCell().getY())+"\n")
            elif Enemy.getCell().getX() < 10 and Enemy.getCell.getY() >= 10 :
                f.write("0"+str(Enemy.getCell().getX())+str(Enemy.getCell().getY())+"\n")
            elif Enemy.getCell().getX() >= 10 and Enemy.getCell.getY() < 10 :
                f.write(str(Enemy.getCell().getX())+"0"+str(Enemy.getCell().getY())+"\n")
            else :
                f.write(str(Enemy.getCell().getX())+str(Enemy.getCell().getY())+"\n")
        
        #numero de armas
        f.write(str(len(finalWeapons)))
        
        #por cada arma
        numComponents = self.__dmech.getEquippedComponentsNumber() 
        numActuators = self.__dmech.getActuatorsNumber()
        for i in range(finalWeapons):
            
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
            loca = self.__dmech.location[itemLocation]
            encontrado = False
            for j in range(loca.getSlotNumber) and not(encontrado):
                if loca.slot[j].getCode() == finalWeapons[i].getCode():
                    encontrado = True
                    f.write(str(j)+"\n")
            
            #Disparo a doble cadencia -> siempre false, no es buena estrategia
            f.write("False"+"\n")
            if finalWeapons[i].getType() == "Energ�a":
                f.write("-1"+"\n")
                f.write("-1"+"\n")
            else:
                numComponents = self.__dmech.getEquippedComponentsNumber() 
                numActuators = self.__dmech.getActuatorsNumber()
                for j in range(numComponents):
                    if self.__dmech.component[j].getWeaponCode() == finalWeapons[i].getCode() :
                        ammunitionCode = self.__dmech.component[j].getCode()
                        for h in range(numActuators):
                            if self.__dmech.actuator[h].getCode() == ammunitionCode:
                                itemLocation = self.__dmech.actuator[h].getItemLocation()
                                if itemLocation == 0 : f.write("BI"+"\n")
                                elif itemLocation == 1: f.write("TI"+"\n")
                                elif itemLocation == 2: f.write("PI"+"\n")
                                elif itemLocation == 3: f.write("PD"+"\n") 
                                elif itemLocation == 4: f.write("TD"+"\n")
                                elif itemLocation == 5: f.write("BD"+"\n")
                                elif itemLocation == 6: f.write("TC"+"\n")
                                elif itemLocation == 7: f.write("CAB"+"\n")
                    
                            #numero de slot donde esta la municion
                                loca = self.__dmech.location[itemLocation]
                                encontrado = False
                                for j in range(loca.getSlotNumber) and not(encontrado):
                                    if loca.slot[j].getCode() == ammunitionCode :
                                        encontrado = True
                                        f.write(str(j)+"\n")
            
            #Hexagono objetivo del arma
            if Enemy.getCell().getX() < 10 and Enemy.getCell.getY() < 10 :
                f.write("0"+str(Enemy.getCell().getX())+"0"+str(Enemy.getCell().getY())+"\n")
            elif Enemy.getCell().getX() < 10 and Enemy.getCell.getY() >= 10 :
                f.write("0"+str(Enemy.getCell().getX())+str(Enemy.getCell().getY())+"\n")
            elif Enemy.getCell().getX() >= 10 and Enemy.getCell.getY() < 10 :
                f.write(str(Enemy.getCell().getX())+"0"+str(Enemy.getCell().getY())+"\n")
            else :
                f.write(str(Enemy.getCell().getX())+str(Enemy.getCell().getY())+"\n")
                
            f.write("Mech"+"\n")
            f.close()
                                
    
    def shootWeapons(self, Enemy, temp, choiseWeapons) :
        cumulativeTemp = 0
        #ordenamos las armas lanzables por calidad
        for i in range(choiseWeapons):        
            """Ordena la lista por el metodo burbuja mejorado y 
         ademas sale del ciclo de pasadas, en cuanto detecta 
         que al final de una pasada no se realizaron 
         intercambios.""" 
            intercambios=1 
            pasada=1 
            while pasada<len(choiseWeapons) and intercambios==1 : 
                intercambios=0 
                for i in range(0,len(choiseWeapons)-pasada):  
                    if (choiseWeapons[i].getHarm()/choiseWeapons[i].getHeaT()) >  (choiseWeapons[i+1].getHarm()/choiseWeapons[i+1].getHeaT()): 
                        choiseWeapons[i], choiseWeapons[i+1] = choiseWeapons[i+1], choiseWeapons[i] 
                        intercambios=1  
                    pasada += 1 
        #compruebo cuantas armas de las seleccionadas puedo disparar sin superar el limite de calor    
        finalWeapons = None
        numWeapons = 0
        for i in range(choiseWeapons):
            if not(cumulativeTemp + choiseWeapons[i].getHeat() > temp):
                cumulativeTemp = cumulativeTemp + choiseWeapons.getHeat()
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
        disWeapons = None
        for  i in range(self.__dmech.getEquippedComponentsNumber() ):
            distance = euclideanDistance(self.__player.getCell, Enemy.getCell() )
            if (distance <= self.__dmech.component[i].longDistance) and self.__dmech.component[i].operativeTeam :
                disWeapons.append(self.__dmech.component[i])
        return disWeapons
                                           
    
    def enemyMoreNear(self, enemysList, distance):
        i = 0
        min = 0
        distance = euclideanDistance(self.__player.getCell(), enemysList[0].getCell())
        while i < len(enemysList):
            if (distance > (euclideanDistance(self.__player.getCell(), enemysList[i].getCell())) ):
                distance = euclideanDistance(self.__player.getCell(), enemysList[i].getCell())
                min = i
            i = i +1
        return i
             

    def visionLine(self, enemy):
        GroundPlayer = self.__player.getGround()
        GroundEnemy = self.__mechs.mechSet[enemy.playerNumber].getGround()
        cellSource = self.__player.getCell()
        cellGoal = self.__mechs.mechSet[enemy.playerNumber].getCell()
        execute = "LDyC.exe "+self.__fichBoard+" "+cellSource+" "+GroundPlayer+" "+cellGoal+" "+GroundEnemy
        
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
        
        
def str2bool(string):
    if string.strip().lower() in ('yes', '1', 'true', 'si'):
        return True
    elif string.strip().lower() in ('no', '0', 'false'):
        return False
    else:
        return "Error: Not boolean"

def euclideanDistance(self, c1, c2):
    return sqrt(((c2.getX()-c1.getX())*(c2.getX()-c1.getX())+((c2.getY()-c1.getY())*(c2.getY()-c1.getY()))

        