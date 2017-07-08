#!/usr/bin/env python
######################################################################
# This program allows to get status of all the git repositories
# that the user has, assuming they all reside in the same directory.
######################################################################


# import os
# from subprocess import call
from Tkinter import Tk
from tkFileDialog import askopenfilename, askdirectory

Tk().withdraw()
# we don't want a full GUI, so keep the root window from appearing
# filename = askopenfilename()
foldername = askdirectory()
# show an "Open" dialog box and return the path to the selected file
print(foldername)
