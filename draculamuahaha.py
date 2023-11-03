#!/usr/bin/env python3

with open("dracula.txt", "r") as draculaobj:
    vampcount = 0
    draculalines = draculaobj.readlines()

    for line in draculalines:
        if "vampire" in line.lower():
            vampcount += 1
            with open("vampytimes.txt", "a") as vampobj:
                print(line, end="", file=vampobj)
    print(vampcount)

