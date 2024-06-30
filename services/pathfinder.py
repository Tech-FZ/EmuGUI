import re

#exec_folder = __file__.replace("emugui.py", "").replace("emugui.exe", "").replace("emugui", "")

def retrieveExecFolderTest():
    test_dir = "/progr/emugui/emugui.exe"
    print(test_dir)
    exec_dir = ""
    
    if test_dir.endswith(".py"):
        exec_dir = re.sub("emugui.py$", "", test_dir)

    elif test_dir.endswith(".exe"):
        exec_dir = re.sub("emugui.exe$", "", test_dir)

    else:
        exec_dir = re.sub("emugui$", "", test_dir)

    print(exec_dir)

def retrieveExecFolder():
    print(__file__)
    exec_dir = re.sub("services/pathfinder.py$", "", __file__)
    
    """ if __file__.endswith(".py"):
        exec_dir = re.sub("emugui.py$", "", __file__)

    elif __file__.endswith(".exe"):
        exec_dir = re.sub("emugui.exe$", "", __file__)

    else:
        exec_dir = re.sub("emugui$", "", __file__) """

    return exec_dir

#retrieveExecFolder()