# Task 4 Square Root 

This is task 05, where we are asked to write a program that will take in a positive floating point integer, and output it's approximate square root.  
 

## Summary of the program

This is a program which takes in a positive floating-point number as input, and outputs the approximation of its square root.

Newton's method was researched and used in this program to find the square root: 
```python
a = float(value)  
    for i in range(number_iters):
        value = 0.5 * (value + a / value)
    return value  
```

This was then used to created a function for square root, named 'sqRt' within the program. When a positive integer is entered, the function will produce it's approx. square root.


## Running the Program 
```python
py squareroot.py
```
For the purpose of this program, the user is asked to put input the value ```14.5```.

The expected out for this is ```3.8```.




## References
https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d

https://www.w3schools.com/python/python_functions.asp
## Author
Shane Kelly 
