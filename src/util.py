import os

def makeDir(dir_name):
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        pass
