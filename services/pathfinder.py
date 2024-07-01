import re
import platform

def retrieveExecFolder():
    print(__file__)
    exec_dir = ""

    if platform.system() == "Windows":
        if __file__.endswith(".py"):
            exec_dir = re.sub(r"services\\pathfinder.py$", "", __file__)

        elif __file__.endswith(".pyc"):
            exec_dir = re.sub(r"_internal\\services\\pathfinder.pyc$", "", __file__)

    """ else:
        if __file__.endswith(".py"):
            exec_dir = re.sub("services/pathfinder.py$", "", __file__)

        elif __file__.endswith(".pyc"):
            exec_dir = re.sub("_internal/services/pathfinder.pyc$", "", __file__) """

    return exec_dir

#retrieveExecFolder()