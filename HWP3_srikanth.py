''' script to generate the maximum number of the 3 entered values
    author: srikanth '''

def maxOfThree(): #function to calculate the max of three numbers
    num1 = float(input('enter the first number: '))       #taking the input and storing it in a variable. 
    num2 = float(input('enter the second number: '))      
    num3 = float(input('enter the third number: '))


    if ( num1 >= num2 ) and ( num1 >= num3 ):       #calculating the highest of the 3 number
        largest = num1
    elif ( num2 >= num1 ) and ( num2 >= num3 ):
        largest = num2
    else:
        largest = num3
    print('The largest number between',num1,',',num2,'and',num3,'is: ',largest)


def main():
    print('script to displays the highest of 3 numbers')
    try:  #try and except block for ValueError if input is not a number.
        maxOfThree()
    except ValueError:
        print('value error enter proper input')
    

if __name__ == "__main__":
    main()