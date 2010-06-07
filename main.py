#!/usr/bin/python

__id__ = "$Id: main.py $"
__version__ = "$Revision: 15 $"
__date__ = "$Date: 07/06/2010 Sun $"
__author__ = "Maria Carrasco Rodriguez, Francisco Manuel Herrero Perez"
__license__ = "GPL"
__URL__ = "http://code.google.com/p/smart-player/"

import sys
import traceback
import os
import getopt
import Options
import Board
import DefMech
import MechFile
import Initiative
import Movement
import Attack
import EndTurn
import Reaction
 
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
        print "Error: Incorrect number of arguments\n Player Number + Phase"
        return -1
   
    try:
        actualPlayer = int(args[0])
        phase = args[1]

        # Reading the options
        config = Options.Options()
        config.readOptions("../ficheros/configJ"+str(actualPlayer)+".sbt")

        # Reading the mech file
        mechs = MechFile.MechFile()
        mechs.readMechFile("../ficheros/mechsJ"+str(actualPlayer)+".sbt")

        # Reading the board
        board = Board.Board(mechs.enemys_cell())
        board.readBoard("../ficheros/mapaJ"+str(actualPlayer)+".sbt")

        # Reading initiative file
        ini = Initiative.Initiative()
        ini.readInitiative("../ficheros/iniciativaJ"+str(actualPlayer)+".sbt")

 

        # Reading defMechs
        defM = []
        for x in range(mechs.mechNumber):
            M = DefMech.DefMech()
            M.readDefMech("../ficheros/defmechJ" + str(actualPlayer) + "-" + str(x) + ".sbt")
            defM.append(M)
            M = None



    
        # For each phase
        if phase == "Movimiento":
            movement (actualPlayer,board, mechs, ini)
        elif phase == "Reaccion":
            reaction (actualPlayer, board, mechs, ini)
        elif phase == "AtaqueArmas":
            weaponsAttack (actualPlayer, board, mechs, defM)
        elif phase == "AtaqueFisico":
            physicalAttack (actualPlayer, board, mechs, defM)
        elif phase == "FinalTurno":
            turnEnd (actualPlayer)
        else: 
            print "Incorrect Phase!!"
            return -2

        os.system("pause")
    
    except:
        print "Error"
        traceback.print_exc(file=sys.stdout)
        
def movement (actualPlayer, board, mechs, ini):
    strategy = Movement.Movement(actualPlayer, board, mechs, ini)
    strategy.nextMove()

def reaction (actualPlayer, board, mechs, ini):
    re = Reaction.Reaction(actualPlayer, board, mechs, ini)
    re.calculate_reaction()

def weaponsAttack (actualPlayer, board, mechs, defM):
    attack = Attack.Attack(actualPlayer, mechs, defM, "mapaJ"+str(actualPlayer)+".sbt", board)
    attack.weaponsAttack ()
    print "Atatck - W"

def physicalAttack (actualPlayer, board, mechs, defM):
    attack = Attack.Attack(actualPlayer, mechs, defM, "mapaJ"+str(actualPlayer)+".sbt", board)
    attack.physicalAttack ()
    print "Atatck - P"

def turnEnd (actualPlayer):
    end = EndTurn.EndTurn(actualPlayer)
    end.printAction()

if __name__ == "__main__":
    main()

