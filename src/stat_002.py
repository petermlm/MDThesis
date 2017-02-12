#!/usr/bin/env python3

# =============================================================================
# Get the domain for a few fields of the courses
# =============================================================================


import numpy as np
import pandas
from matplotlib import pyplot


import data

def uniq(cg, field):
    print("%s:" % (field))

    for i in cg[field].unique():
        print("\t%s" % (i))

    print("")


if __name__ == "__main__":
    # Load data
    cg = data.load(data.CoursesGeneral)

    uniq(cg, "Department")
    uniq(cg, "Cycle")
    uniq(cg, "Regime")
    uniq(cg, "Credits")
    uniq(cg, "Degree")
    uniq(cg, "Semester")
    uniq(cg, "Season")
    uniq(cg, "Type")
