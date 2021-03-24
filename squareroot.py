# Write a program that takes a positive floating-point number as input and outputs an 
# approximation of its square root.
#First, I must create the function for square root, using newtons method for estimating square roots 
#This was firstly done on a seperate program named 'funtion.py'
#I will then write to code to allow the user to enter the number and along with output print

number = float(input("Please enter a positive number: "))  #coding for numer user enters 

#How to write code for Newtons method was found using the below link
#https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d
#Function reading: https://www.w3schools.com/python/python_functions.asp

def sqRt(value, number_iters = 10): #value = number - number_iters is the no of times the value will be itterated
    a = float(value)  
    for i in range(number_iters):
        value = 0.5 * (value + a / value)
    return value 

print("The square root of {} is approx. {}".format(number, sqRt(number)))
