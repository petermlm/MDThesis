#!/usr/bin/env python3

# =============================================================================
# Gets the number of courses per degree and the number of courses per degree
# and semester
# =============================================================================


import numpy as np
import pandas
from matplotlib import pyplot


import data


if __name__ == "__main__":
    # Load data
    df = data.load(data.CoursesGeneral)

    # Get by degree
    by_deg_df = df[["Degree", "CourseCodeMoodle"]]
    by_deg = by_deg_df.groupby("Degree").agg("count")

    # Get by degree and semester
    by_deg_sem_df = df[["Degree", "CourseCodeMoodle", "Semester"]]
    by_deg_sem = by_deg_sem_df.groupby(["Degree", "Semester"]).agg("count")

    # Print
    print(by_deg)
    print(by_deg_sem)
