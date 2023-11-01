#!/usr/bin/env python3

def main():
    
    #create the counter
    round = 0

    #start the loop
    while True:
        #increment the counter
        round = round + 1
        
        #print the user
        print('Finish the movie title, "Monty Python\'s The Life of ______"')
        
        #read in the user's answer
        answer = input("Your guess--> ")
        
        #if the user answered correctly
        if answer == 'Brian':
            print('Correct')
            break
        #if the that was the last try
        elif round==3:
            print("Sorry, the answer was Brian.")
            break
        #if they still have more tries remaining
        else:
            print("Sorry! Try again!")

    
if __name__ == "__main__":
    main()
