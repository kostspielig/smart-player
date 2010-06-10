#!/usr/bin/python

__id__ = "$Id: EndTurn.py $"
__version__ = "$Revision: 2 $"
__date__ = "$Date: 07/06/2010 Sat  $"
__author__ = "Maria Carrasco Rodriguez, Francisco Manuel Herrero Perez"
__license__ = "GPL"
__URL__ = "http://code.google.com/p/smart-player/"


class EndTurn:
    """ End of Turn File"""

    def __init__ (self, playerN, defmechs, mechs):
        self.playerN = playerN
        self.player = mechs.mechSet[self.playerN]
        self.dmech = defmechs[self.playerN]
        self.log = ""


    def printAction(self):
        self.log = self.log + "FASE DE FINAL TURNO =====================>\n"
        f = open("accionJ"+ str(self.playerN)+".sbt", "w")
       
        f.write(str(0) +"\n") #Numero de radiadores a apagar
        f.write(str(0) +"\n") #Numero de radiadores a encender
        
        if self.player.getStick() == True :
            f.write(str(True) +"\n")
            self.log += "Nos deshacemos del garrote\n"
        else :
            f.write(str(False) +"\n")
            
            
        	
    	cont = 0
    	numComponents = self.dmech.mech.equippedComponentsNumber
        weaponsTrash = []
        if self.dmech.mech.getLArm() == False :
            j = 0	
            while j < numComponents:
                h = 0
            	encontrado = False
                encontrado2 = False
                if 0 == self.dmech.mech.component[j].getItemLocation() :
            	    ammunitionCode = self.dmech.mech.component[j].getWeaponCode()
            	    weaponsTrash.append(self.dmech.mech.component[j])
             	
             	while h < numComponents and not(encontrado):
                    if self.dmech.mech.component[h].getCode() == ammunitionCode:
                        encontrado = True
                        cont = cont + 1
                    h = h + 1
                j = j +1
            
        elif self.dmech.mech.getRArm() == False :
            j = 0
            while j < numComponents :
                h = 0
                encontrado = False
                encontrado2 = False
                if 5 == self.dmech.mech.component[j].getItemLocation():
        	    ammunitionCode = self.dmech.mech.component[j].getWeaponCode()
                    weaponsTrash.append(self.dmech.mech.component[j])
             	
             	while h < numComponents and not(encontrado):
                    if self.dmech.mech.component[h].getCode() == ammunitionCode:
                    	encontrado = True
                        cont = cont + 1
                    h = h + 1
                j = j +1
            
        if cont > 0 :
            f.write(str(cont)+"\n")
            if cont == 1 :
                self.log += "Nos deshacemos de "+str(cont)+" municion\n"
            else:
                self.log += "Nos deshacemos de "+str(cont)+" municiones\n"

            j = 0
            while j < len(weaponsTrash) :
                h = 0
                encontrado = False
                encontrado2 = False
            	ammunitionCode = weaponsTrash[j].getWeaponCode()
             	
             	while h < numComponents and not(encontrado):
                    if self.dmech.mech.component[h].getCode() == ammunitionCode:
                    	encontrado = True
                        itemLocation = self.dmech.mech.component[h].getItemLocation()
                        if itemLocation == 0  : f.write("BI"+"\n")
                        elif itemLocation == 1: f.write("TI"+"\n")
                        elif itemLocation == 2: f.write("PI"+"\n")
                        elif itemLocation == 3: f.write("PD"+"\n")
                        elif itemLocation == 4: f.write("TD"+"\n")
                        elif itemLocation == 5: f.write("BD"+"\n")
                        elif itemLocation == 6: f.write("TC"+"\n")
                        elif itemLocation == 7: f.write("CAB"+"\n")
                        
                        #numero de slot donde esta la municion
                        loca = self.dmech.mech.location[itemLocation]
                        encontrado2= False
                        k = 0
                        while k < loca.getSlotNumber() and not(encontrado2):
               	            if loca.slot[j].getCode() == ammunitionCode :
                                encontrado2 = True
                                self.log += "Municion arrojada\n"
                                f.write(str(k)+"\n")
                            k = k +1
                        h = h +1
                    j = j+1
			
            else:
                self.log += "=====================>\n\n"
	    	f.write(str(0) +"\n")    

        f.close()

    def printLog(self):
        file = open("x50608460.log", "a")
        file.write (self.log)
        file.close()
