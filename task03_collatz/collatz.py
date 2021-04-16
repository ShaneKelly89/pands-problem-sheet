#This is a program that asks the user to input any positive integer
#and outputs the successive values of a calculation 
#Author Shane Kelly
#First thing I must code is the users input number 
#https://stackoverflow.com/questions/42894178/python-validating-user-input 
#https://stackoverflow.com/questions/26198131/check-if-input-is-positive-integer                
while True:        # Running a while true loop to make sure that a positive integer is entered 
    number = input("enter a positive integer: ")
    try:
        val = int(number)
        if val <= 0:             #If a negative integer is entered the code will not run but prompt to enter again
            print("Error: Please enter a positive integer")
            continue
        break
    except ValueError:            #If a non integer is the code will again provide a prompt 
        print("You have not entered an Integer!")
print(val)             #Once a postitive In is entered to loop will break and the code will continue

#I now need to do calculations until the value is equal to 1. 
#For this I will need to run a while loop, and include the conditions mentioned in the task 
#https://realpython.com/python-while-loop/

numberToStop = 1 #Have program end when number is one
while val != numberToStop: #this is telling the program to run following loop when number not equal to 1
    if (val % 2) == 0: 
        val = val / 2     #Here i am dividing even numbers by 2 as per statement 
    else:                      #Can only be odd or even (hence using else statement)
        val = (val * 3) + 1 #Again I am assigning new value to number to x3 +1 
    #print statement to be placed at this line as we want it to show the new value number within the loop 
    print(int(val))
#Found output presenting as float when ran as print(number) so changed to cast as int
