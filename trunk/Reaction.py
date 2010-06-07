#!/usr/bin/python

__id__ = "$Id: Reaction.py $"
__version__ = "$Revision: 1 $"
__date__ = "$Date: 06/06/2010 Sat  $"
__author__ = "Maria Carrasco Rodriguez, Francisco Manuel Herrero Perez"
__license__ = "GPL"
__URL__ = "http://code.google.com/p/smart-player/"


class Reaction:
    """ Reaction Phase """

    def __init__ (self, playerN):
        self.playerN = playerN

    def printAction(self):
        file = open("accionJ"+ str(self.playerN)+".sbt", "w")
        
        file.write(str(0) +"\n")
        file.write(str(0) +"\n")
        file.write(str(False) +"\n")
        file.write(str(0) +"\n")

        file.close()

