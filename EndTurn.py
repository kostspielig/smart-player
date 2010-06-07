#!/usr/bin/python

__id__ = "$Id: EndTurn.py $"
__version__ = "$Revision: 2 $"
__date__ = "$Date: 07/06/2010 Sat  $"
__author__ = "Maria Carrasco Rodriguez, Francisco Manuel Herrero Perez"
__license__ = "GPL"
__URL__ = "http://code.google.com/p/smart-player/"


class EndTurn:
    """ End of Turn File"""

    def __init__ (self, playerN):
        self.playerN = playerN

    def printAction(self):
        file = open("accionJ"+ str(self.playerN)+".sbt", "w")
        
        file.write(str(0) +"\n")
        file.write(str(0) +"\n")
        file.write(str(False) +"\n")
        file.write(str(0) +"\n")

        file.close()

    def printLog(self):
        file = open("x50608460.log", "a")
        file.write (" FASE FIN DE TURNO  ====================>\n")
        file.write (" \n")
        file.write ("<========================================\n")
        file.close ()
        

