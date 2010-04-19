#!/usr/bin/python

__id__ = "$Id: Cell.py $"
__version__ = "$Revision: 1 $"
__date__ = "$Date: 16/04/2010 Fri $"
__author__ = "Maria Carrasco Rodriguez y Francisco Manuel Herrero Perez"
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



class Cell():
    
    def __init__(self):
        self.level = None
        self.ground = None
        self.objects = None
        self.fce = None
        self.collapsedBuilding = None
        self.fire = None
        self.smoke = None
        self.stick = None
        self.faceRiver = []
        self.faceRoad = []

