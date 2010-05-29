#!/usr/bin/python

__id__ = "$Id: main.py $"
__version__ = "$Revision: 1 $"
__date__ = "$Date: 09/05/2010 Sun $"
__author__ = "Maria Carrasco Rodriguez, Francisco Manuel Herrero Perez"
__license__ = "GPL"
__URL__ = "http://code.google.com/p/smart-player/"

import sys
import getopt
import Options
import Board
import DefMech
import MechFile
 
"""
Main Function

"""
def main():
    # parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)
    # process arguments
    if len(args) != 2:
        print "Error: Incorrect number of arguments"
        return -1
   
        
    playerNumber = int(args[0])
    phase = args[1]

    # Reading the options
    config = Options.Options()
    config.readOptions("configJ"+str(playerNumber)+".sbt")

    # Reading the board
    board = Board.Board()
    board.readBoard("mapaJ"+str(playerNumber)+".sbt")

    # Reading the mech file
    mechs = MechFile.MechFile()
    mechs.readMechFile("mechsJ"+str(playerNumber)+".sbt")

    # Reading defMechs
    defM = []
    for x in range(mechs.mechNumber):
        M = DefMech.DefMech()
        M.readDefMech("defmechJ" + str(playerNumber) + "-" + str(x) + ".sbt")
        defM.append(M)
        M = None

    # For each phase
    if phase == "Movimiento":
        movement()
    elif phase == "Reaccion":
        reaction ()
    elif phase == "AtaqueArmas":
        weaponsAttack ()
    elif phase == "AtaqueFisico":
        physicalAttack ()
    elif phase == "FinalTurno":
        turnEnd ()
    else: 
        print "Incorrect Phase!!"
        return -2

if __name__ == "__main__":
    main()

def movement ():
    print "Movement"

def printMovement(playerNumber):
    filename = filename = "accionJ"+ str(playerNumber) +".sbt"
    f = open (filename, "w")
    f.write ("\n")

    f.close()

def reaction ():
    print "Reaction"

def weaponsAttack ():
    print "Atatck - W"

def physicalAttack ():
    print "Atatck - P"

def turnEnd ():
    print "ENDDDDDDDDDDDDDDDDDDDDDDDD"
