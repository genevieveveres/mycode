#!/usr/bin/python3

# notice we no longer need to import urllib.request or json
import requests

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    ## Call the webservice
    groundctrl = requests.get(MAJORTOM)
        # post with requests.post()
        # put with requests.put()
        # delete with requests.delete()
        # head with requests.head()

    ## strip the json off the 200 that was returned by our API
    ## translate the json into python lists and dictionaries
    helmetson = groundctrl.json()

    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(helmetson)

    print('\n\nPeople in Space: ', helmetson['number'])
    for peep in helmetson['people']:
        print(f"{peep['name']} on the {peep['craft']}")

if __name__ == "__main__":
    main()
