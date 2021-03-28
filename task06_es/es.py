#Write a program that reads in a text file and outputs the number of e's it contains.
#The program should take the filename from an argument on the command line.
#What are the steps involved?
#First, create a text file to be used
#Second, test the code to see if can firstly calculate the total number of letters
#Then, figure out how to go through the text and output only the total no of times 'e' appears 

filename = "heaney.txt"
def totalWords():
    with open(filename) as f:
        words = str(f.read()) #placed as string here as file is string 
        return words

poem = totalWords()
#print (poem) was first ran to see if the poem would appear when ran, which it did. 
#I then use my available resources to find out how to count the total no. of a single letter
#https://www.w3schools.com/python/ref_list_count.asp

print(poem.count('e'))