import os


import pandas


data_root = "../../Data/Processed"

CoursesEntriesOverview = os.path.join(data_root, "CoursesEntriesOverview.csv")
CoursesGeneral         = os.path.join(data_root, "CoursesGeneral.csv")
CoursesNoMoodle        = os.path.join(data_root, "CoursesNoMoodle.csv")
CoursesStudents        = os.path.join(data_root, "CoursesStudents.csv")
MoodleLogs             = os.path.join(data_root, "MoodleLogs.csv")
MoodleUsers            = os.path.join(data_root, "MoodleUsers.csv")
Results                = os.path.join(data_root, "Results.csv")
Students               = os.path.join(data_root, "Students.csv")

def load(sheet):
    return pandas.read_csv(sheet)
