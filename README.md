# Getting git status for all repos
This repo will contain scripts for getting `git status` for all the repositories on your machine, assuming they all reside in the same directory.

I know there are [lots](https://stackoverflow.com/questions/18757843/git-status-over-all-repos#18760535) of options for this, made by much more skilled people than myself. But I couldn't miss the oportunity to learn some more programming for this purpose.

I will write first a Python script, but hopefully I will be able to come up with Bash and more alternatives. Just for fun.

**Remark:** The main intention is educational (for myself first) and most probably it will *not* get fancy or "pro", in any sense that may have. So keep that in mind whenever you find issues or annoyances with it.

## Plan
- get the global git repos folder from the user (initialization step -- only first time);
- print status per repo.

### Options
Normally, the program makes sure that the initialization (i.e. getting the global repos folder) is run only the first time. This is done in a straightforward ("dumb?") way: at first run, it writes `yes` in an `.init` file. Then, for subsequent runs, it checks whether there's `yes` in the file. If so, skip the initialization.

However, the program can be run with arguments. 

One argument allows for a `reset` option, that reruns the initialization step.

Another argument allows the user to pass the path to the global git repos folder directly, thus skipping the selection process. If the user so chooses, they will be able to `append` or `replace` the existent path with the input.

One more argument allows for an `append` mode, which can be used to append another directory to the list, through the GUI selection process.

**Examples**
I'm thinking of something like:

```bash
$ python git-global-status -a [-r] /new/path/
# appends [replaces] the /new/path to [with] the existing path

$ python git-global-status -r [-a]
# runs the script, resetting the path [appending to the path]
# and prompting the user to select a new one
# (the initialization process)

$ python git-global-status /central/repos/path/
# initializes the path to argv[1] and 
# prints the git status for all the repos
```
