#!/usr/bin/python3
import requests
import argparse
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("NASA_API_KEY")

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this is our main function
def main():
    ## first grab credentials
    nasacreds = "api_key=" + key

    ## update the date below, if you like
    startdate = "start_date=" + args.start

    enddate = "end_date=" + args.e

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds + "&" + enddate)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Parameters for accessing the Nasa NeoWs")

    parser.add_argument("-s","--start",required=True,type=str,help="Please enter a start date")
    parser.add_argument("-e",type=str,default="",help="optionally, enter an end date")

    args=parser.parse_args()

    main()
