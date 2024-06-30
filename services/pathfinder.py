import re

def retrieveExecFolder():
    print(__file__)
    exec_dir = ""

    if __file__.endswith(".py"):
        exec_dir = re.sub("services/pathfinder.py$", "", __file__)

    elif __file__.endswith(".pyc"):
        exec_dir = re.sub("services/pathfinder.pyc$", "", __file__)

    return exec_dir

#retrieveExecFolder()