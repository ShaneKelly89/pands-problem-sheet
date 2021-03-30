#Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 
# in the range [0, 4] on the one set of axes.
#Author Shane Kelly 
#References: https://www.datacamp.com/community/tutorials/matplotlib-tutorial-python?utm_source=adwords_ppc&utm_campaignid=898687156&utm_adgroupid=48947256715&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=332602034349&utm_targetid=aud-299261629574:dsa-473406587955&utm_loc_interest_ms=&utm_loc_physical_ms=1007850&gclid=Cj0KCQjwmIuDBhDXARIsAFITC_4aOtjurotJy3Z62n1reCp70o3H0AEibJiMz8SwgK-qzyyvhROig2UaApOdEALw_wcB
#https://www.kite.com/python/answers/how-to-make-multiple-plots-on-the-same-figure-in-matplotlib-in-python
import matplotlib.pyplot as plt   #importing needed libraries for task 
import numpy as np 

#First I must code for x (refernce taken from lab)
x = np.array(range(0,4)) # range is 3 

#Now that I created the variable 'x' I will now write the variables f(x), g(x), and h(x).
f = x 
#plt.plot(f)
#plt.show()
g = x ** 2     #( 3 to the power of 2 = 9)
#plt.plot(g)
#plt.show()
h = x ** 3     #(3 to the power of 3 = 27)
#plt.plot(h)
#plt.show()
#Each plot was ran seperately as written to test 
#plt.plot(f,g,h) first attepmt at plot

#Plotting each function to the plot, adding different color for each and label for each.
plt.plot(x, f, color = 'r', label = 'f(x)')  
plt.plot(x, g, color = 'b', label = 'g(x)')
plt.plot(x, h, color = 'y', label ='h(x)')
plt.plot(f,g,h)
plt.legend()       #adding legend so that the labels will appear in the plot. 
plt.title("Task 07 Plotting")
plt.show()