#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import random
import requests
import html

URL= "https://opentdb.com/api.php?amount=10&category=32&difficulty=medium"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()

    for question in data['results']:

        print(html.unescape(question['question']))
        if len(question['incorrect_answers']) == 1:
            useranswer = input('\tTrue or False?  >')
            
            if(useranswer.lower() == question["correct_answer"].lower()):
                print("\tCorrect!")

            else:
                print("\tIncorrect!")
            
        else: 
            answers = [question['correct_answer']]

            for ans in question['incorrect_answers']:
                answers.append(ans)

            random.shuffle(answers)
            anum = 1

            for ans in answers:
                print(f'\t{anum}: {html.unescape(ans)}')
                anum += 1

            print(f'\tAnswer: {html.unescape(question["correct_answer"])}')
if __name__ == "__main__":
    main()
