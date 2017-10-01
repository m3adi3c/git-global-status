# Getting git status for all modified repos
This repo will contain scripts for getting `git status` for all the repositories on your machine, assuming they all reside in the same central directory. If not, you have to specify the paths one by one, for all the repos.

It will only print the statuses for repos that have uncommited changes.

I know there are [lots](https://stackoverflow.com/questions/18757843/git-status-over-all-repos#18760535) of options for this, made by much more skilled people than myself. But I couldn't miss the oportunity to learn some more programming for this purpose.

I will write first a Python script, but hopefully I will be able to come up with Bash and more alternatives. Just for fun.

**Remark:** The main intention is educational (for myself first) and most probably it will *not* get fancy or "pro", in any sense that may have. So keep that in mind whenever you find issues or annoyances with it.


## Requirements
- Python >= 3
- [pipenv](http://docs.pipenv.org/en/latest/#)

## Getting Started

**You should have** `python >= 3` **installed on your machine**. To do that you can follow [this guide]( http://docs.python-guide.org/en/latest/starting/install3/osx/#install3-osx).

1. Install pipenv [pipenv](http://docs.pipenv.org/en/latest/)

``` 
pip install pipenv
```

2. Set Python 3 as the main python version and create the virtualenv by using the command `pipenv --three`

``` 
pipenv --three
```

for installing your default Python version when running `$ python3`.
If you want to run a specific version of python you can use the following command

```
pipenv --python=pythonX.Y
```

where X.Y is Python's version.
For example `pipenv --python=python3.6`.

3. Install all dependencies

```
pipenv install
```

# Description and Use Examples
The "main" program is `git-global-status.py`, which can be run in the general form:

```bash
$ pipenv run python git-global-status.py [action] [mode] [path]
```

The preceeding `pipenv run` marks the fact that the following command is executed under the 
pipenv virtual environment, not the global one. 

The actions are:
- `-r` = reset/initialize the central directory with repos;
- `-a` = append to the list of central directories;

The (optional) mode can be:
- `-s` = run in "silent mode", i.e. without running `git status`.

Example:

```bash
$ pipenv run python git-global-status.py -a -s /one/more/path
# appends /one/more/path to the list of paths
```

With any action or mode, if no explicit path is provided as a last argument, the GUI version will take over and let you select the directory.

If the directories were initialized (i.e. at least once, the program was started with the `-r` action), it can be called without options afterwards, to operate on the same central directory.

Example uses:

```bash
$ python git-global-status.py -r /path/to/central/directory
# initializes the path to /path/to/central/directory

$ python git-global-status.py -a -s /one/more/path
# appends /one/more/path "silently", i.e. will not run git status after

$ python git-global-status.py -r
# will start the GUI selector for central directory and run git status for all the repos in it
```

## Simple Version
Before making the "full version", I made a toy example, `simple_ggstat.py`, which does not take any options or modes.

It can be used like:

```bash
$ python simple_ggstat.py
# open GUI selector for central directory,
# then run git status for the repos in it

$ python simple_ggstat.py /path/to/central/directory
# skip initialization,
# run git status for the repos in the path provided
```


# Screenshots
![Screenshot in action](/scratch/git-global-status.png?raw=true "Program in action")
![Screenshot -rs](/scratch/ggstat-rs.png?raw=true "Silently set path")
