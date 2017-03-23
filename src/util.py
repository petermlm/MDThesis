import os
import sys

def makeDir(dir_name):
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        pass


def outputDirName(num):
    return "stat_%03d_results" % (num)


def title(text):
    print("=" * 50)
    print(text)
    print("=" * 50)
    print("")


def printResults(feats, cls, predicted):
    sys.stdout.write("Features:\t[");
    for i in feats[:-1]:
        sys.stdout.write("%.02f, " % (i));
    sys.stdout.write("%.02f]\n" % (feats[-1]));

    print("Class:\t\t%s" % (cls))
    print("Predicted:\t%s" % (predicted))
    print("")


def printByCondition(condition, df, clf, limit=None):
    count = 0;

    def prepare(df, index=None):
        if index:
            return zip(df[0][:index], df[1][:index])
        return zip(df[0], df[1])

    for feats, cls in prepare(df):
        predicted = clf.predict([feats])

        if condition(feats, cls, predicted):
            printResults(feats, cls, predicted)
            count += 1

        if limit is not None and count >= limit:
            return
