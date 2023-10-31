#!/usr/bin/env python3

def main():
    import random

    #build the lists
    wordbank= ["indentation", "spaces"]
    tlgstudents= ["Bert", "Angel", "Chandan", "Chris", "Gen", "Jojo", "Joseph", "Robert", "Sar", "Zack"]

    #add 4 to our wordbank as directed
    wordbank.append(4)

    #get a student number, either from input or randomly (input commented out)
    #num = input(f"Give me a number between 1 and {len(tlgstudents)}:\n>")
    #num = int(num)
    num = random.randrange(0,(len(tlgstudents)-1))

    #get the name of the randomly selected student
    student_name = tlgstudents[num-1]

    #print out the statement
    print(f"{student_name} always uses {wordbank[-1]} {wordbank[1]} to indent.")

main()
