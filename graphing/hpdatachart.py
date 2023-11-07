#!/usr/bin/python3


import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('Agg')

def hpcsvdata():
    mydata = []

    with open("/home/student/mycode/graphing/hpdata.csv","r") as datafile:
        datafromfile = csv.reader(datafile, delimiter=",")
        for row in datafromfile:
            rowdat = (int(row[0]), int(row[1]), int(row[2]), int(row[3]))
            summary.append(rowdat)
    
    return summary

def main():
    ind = np.arange(N)    # the x locations for the groups
    # the width of the bars: can also be len(x) sequence
    width = 0.35

    # describe where to display p1
    p1 = plt.bar(ind, localnetMeans, width)
    # stack p2 on top of p1
    p2 = plt.bar(ind, wanMeans, widt
    # plt.show() # you can try this on a Python IDE with a GUI if you'd like
    plt.savefig("/home/student/mycode/graphing/2018summary.pdf")
    # save a copy to "~/static" (the "files" view)
    plt.savefig("/home/student/static/2018summary.pdf")

if __name__ == "__main__":
    main()

