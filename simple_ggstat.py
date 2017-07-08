#!/usr/bin/env python
######################################################################
# This program allows to get status of all the git repositories
# that the user has, assuming they all reside in the same directory.
# The "central folder" can be selected either via GUI,
# or passed as argv.
######################################################################


from sys import argv
import os
from subprocess import call
from tkFileDialog import askdirectory
from Tkinter import Tk


init_file = open(".init", 'r+')


def check_do_init():
    """ Write 'yes' to the .init file if run the first time.
    Else, pass """
    line = init_file.readline()
    if "yes" not in line:
        init_file.write("yes")


def gui_init():
    """ Run the program after a GUI selection of central folder."""
    check_do_init()
    gui_get_statuses()


def gui_get_statuses():
    """ Get central folder via GUI,
    run the program,
    print the results """
    Tk().withdraw()
    central_folder = askdirectory()
    print(get_statuses(central_folder))


def get_statuses(c_folder):
    """ Get git status for all the directories
    in the central directory.
    Return the list as a dictionary.
    key: repo
    value: status"""
    repos = os.listdir(c_folder)
    for repo in repos:
        if ".git" in os.listdir(repo):
            this_repo = str(c_folder) + "/" + str(repo) + "/"
            os.chdir(this_repo)
            statuses = {}
            statuses[this_repo] = call(["git status"])
    return statuses


def path_init(path):
    """ Run the program with the path specified as argv[1] """
    check_do_init()
    get_statuses(path)


if len(argv) == 1:
    gui_init()
else:
    path_init(argv[1])

init_file.close()
