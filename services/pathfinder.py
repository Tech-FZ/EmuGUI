import re

def retrieveExecFolder():
    print(__file__)
    exec_dir = re.sub("services/pathfinder.py$", "", __file__)
    return exec_dir

#retrieveExecFolder()