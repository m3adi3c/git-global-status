#!/usr/bin/env python
######################################################################
# This program allows to get status of all the git repositories
# that the user has, assuming they all reside in the same directory.
# call:
# $ python git-global-status [option] [path]
# Example:
# $ python git-global-status -a /new/path
# will append /new/path to the global path of git repos
######################################################################

from sys import argv
import os
from subprocess import call
from tkFileDialog import askdirectory
from Tkinter import Tk

arguments = argv

if len(argv) == 1:
    gui_init()
else:
    if "/" in argv[1]:
        path_init(argv[1])
    elif "-a" in argv[1]:
        if "/" in argv[2]:
            append_path(argv[2])
        else:
            gui_append_path()
    elif "-x" in argv[1]:
        if "/" in argv[2]:
            reset_path(argv[2])
        else:
            gui_reset_path
    elif "-r" in argv[1]:
        if "/" in argv[2]:
            replace_path(argv[2])
        else:
            gui_replace()

init_file = open(".init", "rw")
paths_file = open(".paths", "rw")


def check_do_init():
    line = init_file.readline()
    if "yes" in line:
        return
    else:
        init_file.write("yes")
        return


def gui_init():
    check_do_init()
    gui_get_statuses()


def gui_get_statuses():
    Tk().withdraw
    central_folder = askdirectory()
    print(get_statuses(central_folder))


def get_statuses(c_folder):
    paths_file.write(c_folder)
    repos = os.listdir(c_folder)
    for repo in repos:
        if ".git" in os.listdir(repo):
            this_repo = str(c_folder) + "/" + str(repo) + "/"
            os.chdir(this_repo)
            statuses = {}
            statuses[this_repo] = call(["git status"])
        else:
            next
    return statuses


def path_init(path):
    check_do_init()
    get_statuses(path)


def append_path(path):
    check_do_init()
    old_repos = os.listdir(paths_file.readline())
    paths_file.write("\n", path)
    new_repos = old_repos.append(path)
    print(get_statuses(new_repos))


def gui_append_path():
    Tk().withdraw
    appended_path = askdirectory()




init_file.close()
