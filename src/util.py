import os

def makeDir(dir_name):
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        pass


def outputDirName(num):
    return "stat_%03d_results" % (num)
