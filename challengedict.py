#!/usr/bin/env python3 
import pprint

#create the dictionary
abe={
"Name": "Abraham Lincoln",
"Nationality": "American",
"Religion": "Catholic",
"Political Party": "Republican",
"Education": "Bachelor of Arts",
}

def printKeys():
    allKeys = ""
    for k in abe.keys():
        allKeys = allKeys + k + " |  "
    return allKeys

#establish the function
def main():

    userin=input(f"What information about Honest Abe would you like?\nOptions are: {printKeys()}\n\t>")

    print(abe.get(userin, "That is not one of the options"))

    useradd=input("Would you like to add new data? [Y/N]")
    if(useradd.upper()=="Y"):
        useraddkey=input("Enter what you would like to use for the KEY\n>")
        useraddval=input("Enter what you would like to use for the VALUE\n>")
        abe.update({useraddkey: useraddval})

    userdel=input("Would you like to delete any data? [Y/N]")
    if(userdel.upper()=="Y"):
        userdelkey=input("Enter the KEY of the data you would like to remove\n>")
        abe.pop(userdelkey)

    pprint.pprint(abe)

main()
