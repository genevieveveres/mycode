#!/usr/bin/env python3
## create file object in "r"ead mode

userfile = input("Please provide what file to open: >")

with open(userfile, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    numlines = 0
    for line in configlist:
        numlines +=1
    print(numlines)
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)

