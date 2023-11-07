#!/usr/bin/python3

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():

    ## Ask user for input
    got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

    ## Send HTTPS GET to the API of ICE and Fire character resource
    gotresp = requests.get(AOIF_CHAR + got_charToLookup)

    ## Decode the response
    got_dj = gotresp.json()
    
    print("\nThis character appeared in the following books:")
    for book in got_dj['books']:
        bookresp = requests.get(book)
        bookrespdec = bookresp.json()
        print(bookrespdec['name'])

    print("\nThis character has the following allegiances:")
    for alleg in got_dj['allegiances']:
        allegresp = requests.get(alleg)
        allegrespdec = allegresp.json()
        print(allegrespdec['name'])
     
    if got_dj['name'] != "":
        print(f"\nThis character's name is {got_dj['name']}")
    else:
        print(f"\nThis character goes by:")
        for alias in got_dj['aliases']:
            print(alias)
      

if __name__ == "__main__":
    main()
