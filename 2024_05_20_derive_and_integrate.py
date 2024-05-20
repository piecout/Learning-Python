# -*- coding: utf-8 -*-
"""
Created on %(2024-05-10)

@author: %(Piecout)
inspired by numberphile video :
https://youtu.be/OtYKDzXwDEE?si=zHTfmyc5UdvXmZ7p

"""

"""
print("BEGIN POEM")
print("")
print("The Zen of Python, by Tim Peters")
print("Beautiful is better than ugly.")
print("Explicit is better than implicit.")
print("Simple is better than complex.")
print("Complex is better than complicated.")
print("Flat is better than nested.")
print("Sparse is better than dense.")
print("Readability counts.")
print("Special cases aren't special enough to break the rules.")
print("Although practicality beats purity.")
print("Errors should never pass silently.")
print("Unless explicitly silenced.")
print("In the face of ambiguity, refuse the temptation to guess.")
print("There should be one-- and preferably only one --obvious way to do it.")
print("Although that way may not be obvious at first unless you're Dutch.")
print("Now is better than never.")
print("Although never is often better than *right* now.")
print("If the implementation is hard to explain, it's a bad idea.")
print("If the implementation is easy to explain, it may be a good idea.")
print("Namespaces are one honking great idea -- let's do more of those!")
print("")
print("END POEM")
print("")
print("")
print("")
print("")
"""



import sys
import numpy as np
from functools import reduce
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import matplotlib.ticker as mticker

#plt.close()

#plt.close('all')

#plt.clf()

"""
    if n==0:
        array_factor = [0] 
   # else:
"""


#                       my factors function from scrach works
def prop_factors(n):
    array_factor = [1] 
    if n % np.sqrt(n)==0 and n>1:
        array_factor.append(int(np.sqrt(n))) 
    for i in range(2,int(np.ceil(np.sqrt(n)))):
        if n % i==0:
            array_factor.append(i) 
            array_factor.append(int(n/i)) 
    if n==1 or n==0 :
        array_factor = [1] 
    return array_factor

def aliquot(n):    
    return sum(prop_factors(n))
 
#                       lets make a better function


#list.pop() #.pop() will delete and item in the specified index starting from 0
#if you leave it blank it will delete the last item usefull for me because I want the proper factors instead of normal factors

def factors(n):    #I added -n and sum to a function that calculcaltes factors, I spend the time to understand and test it
    return set(reduce(list.__add__,([i, n//i] for i in range(1,int(n**0.5) + 1) if n % i == 0 ))) 

def aliquot2(n):    #I added -n and sum to a function that calculcaltes factors, I spend the time to understand and test it
    return-n+sum(factors(n))


#print(sum(aliquot2(10)))
#print(10//4)
#afloor division;returns an integer, usefull because I can get something like 4.0, a float that does not play nice w/ my code 





"""


print("Begin test")

#                               test with 1


print("aliquot(0)")
print(aliquot(0))
print("aliquot2(0)")
#print(aliquot2(0))
print("does not work")


print("aliquot(1)")
print(aliquot(1))
print("aliquot2(1)")
print(aliquot2(1))


print("prop_factors(8)")
print(prop_factors(8))
print("aliquot(8)")
print(aliquot(8))
print("aliquot2(8)")
print(aliquot2(8))

#                               test with 24

print("aliquot(24)")
print(aliquot(24))
print("aliquot2(24)")
print(aliquot2(24))

#                               test with 25


print("aliquot(25)")
print(aliquot(25))
print("aliquot2(25)")
print(aliquot2(25))







print("End tests")

"""


#sys.exit("Error message")




"""
#                               test with 1

print("prop_factors(1)")
print(prop_factors(1))


#                               test with 24

print("prop_factors(24)")
print(prop_factors(24))
print("aliquot(24)")
print(aliquot(24))


#                               test with 25

print("prop_factors(25)")
print(prop_factors(25))
print("aliquot(25)")
print(aliquot(25))

"""


lehmer_1=276#or 306
lehmer_2=552
lehmer_3=564
lehmer_4=660
lehmer_5=840
lehmer_6=966
list_lehmer = [lehmer_1,lehmer_2,lehmer_3,lehmer_4,lehmer_5,lehmer_6] 


  
#starting_number=lehmer_4#no convergance has been found yet
#starting_number=25#goes to perfect number 6
#starting_number=14#goes to prime number 7 than goes to one
#starting_number=220#amicable pair goes to 284 than back to 220
#starting_number=18
#starting_number=95#inspiring number
#starting_number=30#intresting deficiant number number
#starting_number=138#intresting deficiant number number
#starting_number=980460#intresting amicable pair
#starting_number=2856 #intresting cycle 28 iterations long
#starting_number=306 #goes to lehmor number
#starting_number=1

list_intresting_S_N = [30,95,138,220,2856,980460] 





    
i = 0
i_min=0




#i_total_max=20#          for testing multiple plots lets just do 20 iterations 

i_max=50#                 for testing multiple plots lets just do 20 iterations 


i = i_min
k=0
k_min=0


#number=starting_number
#print("The starting number is "+str(number))

#print("test")

m_min=1
m_max=1+1000

array_starting_number = [j for j in range(m_min,m_max)]    
#print("min_starting_number:") 
#print(array_starting_number[0])
#print("max_starting_number:") 
#print(array_starting_number[m_max-m_min-1])
#print(array_starting_number[3])


log=0
if m_max > 40:#                   comment out if I want a non log plot
        log=1       #                   comment out if I want a non log plot
        
ay = plt.figure().gca()
ay.yaxis.set_major_locator(MaxNLocator(integer=True))




#print("The starting number is "+str(array_aliquot[0]))

k_max=6#    After 6 perfect numbers in a row the code should stop
diverge=0#  A more elagant way would be to use break instead

#print("begin test")

xx = np.arange(0, 1+(i_max-i_min))
#print(xx)

"""

print("list_lehmer_six:")
print(list_lehmer)


m_max_lehmer=6
m_min_lehmer=276


print("min_lehmer_starting_number:") 
print(list_lehmer[0])
print("max_lehmer_starting_number:") 
print(list_lehmer[m_max_lehmer-1])
print("length of starting_number:") 
print(len(list_intresting_S_N))


print("list_lehmer") 
print(list_lehmer)


m_max_intresting=6
m_min_intresting=30

print("min_starting_number:") 
print(list_intresting_S_N[0])
print("max_starting_number:") 
print(list_intresting_S_N[m_max_intresting-1])
print("length of starting_number:") 
print(len(list_intresting_S_N))

print("list_intresting_S_N") 
print(list_intresting_S_N)



#matplotlib.pyplot.close()

print("begin test")


print(list_intresting_S_N[len(list_intresting_S_N)-1])

print(len(array_starting_number))

print("end test")

"""
# Define a list of non-integer values
'''
values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

# Use a for loop to iterate over the values
for value in values:
    print(value)
'''    

#i_min=-100


"""

dx=0.1
i_min=int(x_min/dx)
"""
x_min=-10

#x_min=0
x_max=10
dx=0.1
i_max=int((x_max-x_min)/dx)



array_x=[] 
array_y=[]
array_y_der=[0]#                                temp value
array_y_int=[0]#                                starting value
y_int=0
for i in range(i_min,i_max+1):    
        x=x_min+i*dx
        array_x.append(x) 
        xx = array_x
        y=x**2
        array_y.append(y) 
        yy = array_y
        if i>i_min:
            y_der=(array_y[i]-array_y[i-1])/dx
            array_y_der.append(y_der) 
            yy_der = array_y_der
            
            
            y_int+=dx*(array_y[i]+array_y[i-1])/2
            array_y_int.append(y_int) 
            yy_int = array_y_int

array_y_der[0]=array_y_der[1]#                   set the first value of the derivative        

plt.plot(xx, yy, label='t^2')
          #                                     Add a title, labels, and other customizations
plt.title("Playing with functions and maybe opperators")
plt.xlabel("Iterations")
plt.ylabel("Value of function")
       #  ay = plt.figure().gca()
       #  ay.yaxis.set_major_locator(MaxNLocator(integer=True))
       
plt.plot(xx, yy_der, label='der(t^2)')
plt.title("Playing with functions and opperators")
plt.xlabel("Iterations")
plt.ylabel("Value of function")       
   
plt.plot(xx, yy_int, label='int(t^2)')
plt.title("Playing with functions and maybe opperators")
plt.xlabel("Iterations")
plt.ylabel("Value of function")


plt.legend()
plt.show()


#print(y_int)

#print((x**3)/3)

print("DONE with intresting numbers")

sys.exit("Completly done")

for m in range(0,len(list_intresting_S_N)):#for m in range(m_min,len(list_intresting_S_N)-1):
    #print("The starting number is "+str(array_starting_number[m-2]))
    number=list_intresting_S_N[m]
    array_aliquot = [list_intresting_S_N[m]] 
    for i in range(i_min,i_max):
        number=aliquot(number)
        array_aliquot.append(number) 
    #    i += 1
       # if number > 10**13:#    Cut it short if the value is too big
        #    diverge+=1
       # if number==aliquot(number):
         #   k+=1#       you dont want perfect numbers forever
 #   print(array_aliquot)
#    yy = np.arange(0, 1+(i_max-i_min))+m
    yy = array_aliquot
#    yy[i_max]=0
    if log == 1:
        yy = np.log10(array_aliquot)       
    else:
        yy = array_aliquot    
    plt.plot(xx, yy, label='Starting number '+str(list_intresting_S_N[m]))
     # Add a title, labels, and other customizations
    plt.title("Aliquot series with intresting starting numbers")
    plt.xlabel("Iterations")
    plt.ylabel("Value of aliquot series")
  #  ay = plt.figure().gca()
  #  ay.yaxis.set_major_locator(MaxNLocator(integer=True))
    if i_max < 30:
        plt.ticklabel_format(style='plain', axis='x', useOffset=False)
    # plt.plot(range(1, 3), logger.acc)
        plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))
    if log == 1:
        plt.ylabel("Log_10 of the value of aliquot series")   
    else:
        plt.ylabel("The value of aliquot series")




plt.legend()
plt.show()

print("DONE with intresting numbers")



#sys.exit("Error message")

i_max=50
xx = np.arange(0, 1+(i_max-i_min))

"""
x = [1, 2, 3, 4, 5]
y1 = [1, 2, 3, 4, 5]
y2 = [5, 4, 3, 2, 1]

# Create the graph
plt.plot(x, y1, label='Line 1')
plt.plot(x, y2, label='Line 2')

# Create the legend
plt.legend()

# Show the graph
plt.show()
"""

for m in range(0,len(list_lehmer)):
    #print("The starting number is "+str(array_starting_number[m-2]))
    number=list_lehmer[m]
    array_aliquot = [list_lehmer[m]] 
    for i in range(i_min,i_max):
        number=aliquot(number)
        array_aliquot.append(number) 
    #    i += 1
       # if number > 10**13:#    Cut it short if the value is too big
        #    diverge+=1
       # if number==aliquot(number):
         #   k+=1#       you dont want perfect numbers forever
 #   print(array_aliquot)
#    yy = np.arange(0, 1+(i_max-i_min))+m
    yy = array_aliquot
#    yy[i_max]=0
    if log == 1:
        yy = np.log10(array_aliquot)       
    else:
        yy = array_aliquot    
    plt.plot(xx, yy, label='Starting number '+str(list_lehmer[m]))
     # Add a title, labels, and other customizations
    plt.title("Aliquot series with lehmer numbers as starting numbers")
    plt.xlabel("Iterations")
    plt.ylabel("Value of aliquot series")
  #  ay = plt.figure().gca()
  #  ay.yaxis.set_major_locator(MaxNLocator(integer=True))
    if i_max < 30:
        plt.ticklabel_format(style='plain', axis='x', useOffset=False)
    # plt.plot(range(1, 3), logger.acc)
        plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))
    if log == 1:
        plt.ylabel("Log_10 of the value of aliquot series")   
    else:
        plt.ylabel("The value of aliquot series")
        
plt.legend()        
plt.show()        
print("DONE with lehmer")
        
i_max=50
xx = np.arange(0, 1+(i_max-i_min))


for m in range(m_min,len(array_starting_number)+1):
    #print("The starting number is "+str(array_starting_number[m-2]))
    number=array_starting_number[m-m_min]
    array_aliquot = [array_starting_number[m-m_min]] 
    for i in range(i_min,i_max):
        number=aliquot(number)
        array_aliquot.append(number) 
    #    i += 1
       # if number > 10**13:#    Cut it short if the value is too big
        #    diverge+=1
       # if number==aliquot(number):
         #   k+=1#       you dont want perfect numbers forever
 #   print(array_aliquot)
#    yy = np.arange(0, 1+(i_max-i_min))+m
    yy = array_aliquot
#    yy[i_max]=0
    if log == 1:
        yy = np.log10(array_aliquot)       
    else:
        yy = array_aliquot    
    plt.plot(xx, yy)
     # Add a title, labels, and other customizations
    plt.title("Aliquot series with starting numbers " + str(m_min)+" to "+str(len(array_starting_number)))
    plt.xlabel("Iterations")
    plt.ylabel("Value of aliquot series")
  #  ay = plt.figure().gca()
  #  ay.yaxis.set_major_locator(MaxNLocator(integer=True))
    if i_max < 30:
        plt.ticklabel_format(style='plain', axis='x', useOffset=False)
    # plt.plot(range(1, 3), logger.acc)
        plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))
    if log == 1:
        plt.ylabel("Log_10 of the value of aliquot series")   
    else:
        plt.ylabel("The value of aliquot series")
        
        

plt.show()
print("DONE")
sys.exit("Completly done")

#print(len(list_lehmer))
#list_intresting_S_N

