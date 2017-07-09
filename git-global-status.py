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

"""
This is the documentation
"""


from __future__ import print_function
from sys import argv
import os
from subprocess import check_output
from tkFileDialog import askdirectory
from Tkinter import Tk


init_file = open(".init", "r+")


def run_w_paths():
    """ Run the program, using the paths
    stored in the .paths file. """
    with open(".paths", "r") as pf:
        for line in pf:
            if "/" not in line:
                print("""
                Central directory not initialized.
                Rerun with -r [path]. """)
                return
            else:
                pretty_print_mod(get_statuses(line.rstrip()))


def path_init(path):
    """ Initialize the paths with given path. """
    check_do_init()
    with open(".paths", 'w') as pfile:
        pfile.truncate()
        print(path, file=pfile)
    run_w_paths()


def gui_silent_reset():
    """ Reset/initialize paths via GUI and NOT get statuses. """
    Tk().withdraw()
    central_folder = askdirectory()
    with open(".paths", 'w') as pfile:
        pfile.truncate()
        print(central_folder, file=pfile)


def gui_reset():
    """ Reset/initialize paths via GUI and get statuses. """
    gui_silent_reset()
    run_w_paths()


def gui_silent_append():
    """ Append path selected via GUI and NOT get statuses. """
    Tk().withdraw()
    central_folder = askdirectory()
    with open(".paths", 'a') as pfile:
        print(central_folder, file=pfile)


def gui_append():
    """ Append path selected via GUI to central paths and get statuses.  """
    gui_silent_append()
    run_w_paths()


def silent_path_reset(path):
    """ Reset/initialize paths via argv and NOT get statuses. """
    with open(".paths", 'w') as pfile:
        pfile.truncate()
        print(path, file=pfile)


def path_reset(path):
    """ Reset/initialize paths via argv and get statuses. """
    silent_path_reset(path)
    run_w_paths()


def silent_path_append(path):
    """ Append path passed as argv to central paths and NOT get statuses. """
    with open(".paths", 'a') as pfile:
        print(path, file=pfile)


def path_append(path):
    """ Append path passed as argv to central paths and get statuses. """
    silent_path_append(path)
    run_w_paths()


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
        if os.path.isdir(abs_repo):
            if ".git" in os.listdir(abs_repo):
                this_repo = str(c_folder) + "/" + str(repo) + "/"
                os.chdir(this_repo)
                statuses[this_repo] = check_output("git status", shell=True)
    return statuses


def check_do_init():
    """ Write 'yes' to the .init file
    if run for the first time.
    Else, pass. """
    init_line = init_file.readline()
    if "yes" not in init_line:
        init_file.write("yes")


def pretty_print_dict(d):
    """ Print all the repositories
    and their git statuses. """
    for i in d:
        print("REPO: " + str(i))
        print("STATUS: " + str(d[i]))
        print("------------------------------")


def pretty_print_mod(d):
    """ Print only the repos
    that have changes. """
    print()
    for i in d:
        if "nothing to commit" not in d[i]:
            print("REPO: " + str(i))
            print("STATUS: " + str(d[i]))
            print("------------------------------")


if len(argv) == 1:
    run_w_paths()
elif len(argv) == 2:
    if "/" in argv[1]:
        path_init(argv[1])
    elif "-r" in argv[1]:
        gui_reset()
    elif "-a" in argv[1]:
        gui_append()
elif len(argv) == 3:
    if "-r" in argv[1]:
        if "/" in argv[2]:
            path_reset(argv[2])
        elif "-s" in argv[2]:
            gui_silent_reset()
    if "-a" in argv[1]:
        if "/" in argv[2]:
            path_append(argv[2])
        elif "-s" in argv[2]:
            gui_silent_append()
elif len(argv) == 4:
    if "-s" in argv[2]:
        if "-r" in argv[1]:
            if "/" in argv[3]:
                silent_path_reset(argv[3])
        if "-a" in argv[1]:
            if "/" in argv[3]:
                silent_path_append(argv[3])
else:
    print("Invalid arguments. Check program documentation and retry.")

init_file.close()


print("========== PROGRAM TERMINATED ==========")
