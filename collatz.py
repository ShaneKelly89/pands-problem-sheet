#This is a program that asks the user to input any positive integer
#and outputs the successive values of a calculation 
#Author Shane Kelly
#First thing I must code is the users input number 

number = int(input("enter a positive integer: ")) 
print(number)
#I now need to do calculations until the value is equal to 1. 
#For this I will need to run a while loop, and include the conditions mentioned in the task 
#https://realpython.com/python-while-loop/

numberToStop = 1 #Have program end when number is one
while number != numberToStop: #this is telling the program to run following loop when number not equal to 1
    if (number % 2) == 0: 
        number = number / 2     #Here i am dividing even numbers by 2 as per statement 
    else:                      #Can only be odd or even (hence using else statement)
        number = (number * 3) + 1 #Again I am assigning new value to number to x3 +1 
    #print statement to be placed at this line as we want it to show the new value number within the loop 
    print(int(number))
#Found output presenting as float when ran as print(number) so changed to cast as int
