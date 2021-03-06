#!/usr/bin/env python
######################################################################
# This program allows to get status of all the git repositories
# that the user has, assuming they all reside in the same directory.
# The "central folder" can be selected either via GUI,
# or passed as argv.
#
# Examples:
#
# $ python simple_ggstat.py
#   Will open the interface to select central folder
#   then print git status
#
# $ python simple_ggstat.py /path/to/central/folder
#   will print directly git status
######################################################################

""" simple_ggstat -- Getting git status for repos in a folder

This program allows you to get the git status of all
the repos that are stored in a folder.

The folder can be initialized either via a GUI,
or if run with a path argument, it will initialize the
central directory to that path.
"""

from sys import argv
import os
from subprocess import check_output
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
    pretty_print_mod(get_statuses(central_folder))
#   pretty_print_dict(get_statuses(central_folder))


def get_statuses(c_folder):
    """ Get git status for all the directories
    in the central directory.
    Return the list as a dictionary.
    key: repo
    value: status"""
    repos = os.listdir(c_folder)
    os.chdir(c_folder)
    repos.remove('.DS_Store')
    statuses = {}
    for repo in repos:
        abs_repo = str(c_folder) + "/" + str(repo)
        if ".git" in os.listdir(abs_repo):
            this_repo = str(c_folder) + str(repo) + "/"
            os.chdir(this_repo)
            statuses[this_repo] = check_output("git status", shell=True)
    return statuses


def pretty_print_dict(d):
    """ Print all the repositories
    and their git statuses. """
    for i in d:
        print("REPO: " + str(i))
        print("STATUS: " + str(d[i]))
        print("------------------------------")


def pretty_print_mod(d):
    """ Print only the repositories
    that have changes. """
    for i in d:
        if "nothing to commit" not in d[i]:
            print("REPO: " + str(i))
            print("STATUS: " + str(d[i]))
            print("------------------------------")


def path_init(path):
    """ Run the program with the path specified as argv[1] """
    check_do_init()
    pretty_print_mod(get_statuses(path))
    # pretty_print_dict(get_statuses(path))


if len(argv) == 1:
    gui_init()
else:
    path_init(argv[1])

init_file.close()
