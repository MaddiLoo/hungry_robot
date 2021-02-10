#This program will determine what dad-bot will make me for dinner

import sys

#Imports easygui and geobc from the python library
sys.path.append(r'\\spatialfiles.bcgov\work\ilmb\dss\dsswhse\Tools and Resources\Scripts\Python\Library')
import easygui, geobc

#sys.argv = ['']
from easygui.boxes import utils
from Tkinter import *
import tkFileDialog as tk_MyFileDialog
utils.tk_FileDialog = tk_MyFileDialog

dinner = easygui.buttonbox("Dad I'm hungry!!!", "WHAT IS FOR DINNER?!", ['Pancakes', 'Mac and Cheese', 'Cookies', 'Cheeseburger'])

msg = dinner
tle = "DINNER HAS BEEN DETERMINED AS:"

response = easygui.msgbox(msg, tle)
