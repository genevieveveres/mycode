#!/usr/bin/python3
import requests
import argparse
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("NASA_API_KEY")

## Define NEOW URL
CATURL = "https://eonet.gsfc.nasa.gov/api/v2.1/categories"

# this is our main function
def main():
    ## first grab credentials
    nasacreds = "api_key=" + key

    # make a request with the request library
    catrequest = requests.get(CATURL)
    catdata = catrequest.json()
    
    for cat in catdata["categories"]:
        thecatrequest = requests.get(CATURL +"/"+str(cat["id"])+"?days="+str(args.d))
        thecatdata = thecatrequest.json()

        print(f"There have been {len(thecatdata['events'])} {cat['title']} events in the last {str(args.d)} days")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Parameters for accessing the Nasa EONet")
    parser.add_argument("-d",type=int,default=20,help="Please how many days you would like to look back. The default is 20.") 
    args=parser.parse_args()

    main()
