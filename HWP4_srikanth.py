'''python script to take user input and compare it to random value from 0 to 20
    author srikanth'''

import random  #random library


def numtest(number,guess):  #function for comparing the user guess to the generated number
    while guess > 0 and guess < 21:
        if guess == number:
            print("good guess")
            return 0
        elif guess > number:
            print("guess is higher than the number. try lower")
            return 1
        elif guess < number:
            print("guess is lower than the number. try higher")
            return -1
    else:
        print("guess isnt in range. try again")        


def main():
    name = input("what is your name?")
    print("HI! ", name, ", I am thinking of a number between 1 and 20. can you guess it? ")
    number = random.randint(1 , 20)  #generate a random number from 1 to 20
    guesses=0  #counter to keep the count of guesses
    y=322  #assigned random value to avoide out of bound error in the first iteration
    while True :
        try: #try and catch block for exception handeling
            guess = int(input("enter guess: ")) 
            y= numtest(number,guess)            
        except ValueError:
            print("must enter only numbers")
        guesses = guesses + 1     
        if y == 0:
            print("the number was ", number, " you got it in " , guesses , "attempts")
            break
        elif guesses == 6 :
            print("sorry ", name , "the number i was thinking of was ", number)
            break
    
    
if __name__ == "__main__":
    main()