"""python script to convert marks to grades
   author: srikanth"""

flag = "1" #initilaze flag
while flag == "1": #loop whole script if flag is = 1
    try:   
        marks = float(input("please enter the score that you have recieved in the quiz : ")) #takes input and converts it to float
        if marks > 100:
            print("invalid input score cant be greater than 100")
        elif marks >= 93:
            print("you have received A grade")
        elif marks >= 90:
            print("you have received A- grade")
        elif marks >= 87:
            print("you have received B+ grade")
        elif marks >= 83:
            print("you have received B grade")
        elif marks >= 80:
            print("you have received B- grade")
        elif marks >= 70:
            print("you have received C grade")
        elif marks >= 0:
            print("you have recieved F grade")
        elif marks < 0:
            print("invalid input. score cant be less than 0")
    except ValueError: #exception for when a string is entered.
        print ("error the entered number should be a number not a string")
    
    flag = input("press 1 to input again press any key to quit : ") #input to get the new flag value
    if flag == "1":
        print("\n") #to leave an empty line between two different score
        continue  #while loop will repeat again if entered flag value is 1.
    else:
        print("have a good day")