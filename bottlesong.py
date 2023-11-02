#!/usr/bin/env python3
num=100

while True:
    try:
        num = int(input("How many bottles of beer would you like there to be on the wall? > "))
        assert 0 < num <= 100
        break
    except:
        print("That was not valid fam")

for n in range(num,1,-1):
    print(f"{n} bottles of beer on the wall!\n{n} bottles of beer!\nYou take one down, pass it around\n{n-1} bottles of beer on the wall!")
