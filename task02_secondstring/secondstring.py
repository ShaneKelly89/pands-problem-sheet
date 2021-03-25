#This program will input a string and output every second letter in 
#reverse order 
#Author Shane Kelly

rawString = input("please enter a string:")
reverseString = rawString[::-1] #[::-1] loops through the string backwards (-1)
#and stores the result in the reverseString variable
#https://www.w3schools.com/python/python_howto_reverse_string.asp
#https://scipython.com/book/chapter-2-the-core-python-language-i/examples/string-striding/

#print("Reverse string :{}".format(reverseString)) 
#Ran here to test provisionally to test for reverseString. Output below.
#please enter a string: The quick brown fox jumps over the lazy dog.
#Reverse string :.god yzal eht revo spmuj xof nworb kciuq ehT 

reverseString = rawString[::-2] 
print("Reverse string :{}".format(reverseString)) 

#This code can be improved by running: 
# reverseString = rawString[::-2] so that we loop through every second letter in reverse.