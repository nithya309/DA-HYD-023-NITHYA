import modules
print(dir(modules))
'''
print(type(modules.details))
print(type(modules.greeting))

print(modules.greeting())
print(modules.details)
#we can access function/datatypes using . operator

modules.details['subject'] = ['python','SQL','EDA','PowerBI','Excel','Stats']
print(modules.details.keys())
'''
'''
# we can use from keyword to access desired methods/datatypes
from modules import details
print(details)
#print(greeting()) as we didnot import it raises NameError

details['subject'] = ['python','SQL','EDA','PowerBI','Excel','Stats']
print(details)
'''
#we want to access group of methods/datatypes we can use command
'''
from modules import details,greeting
print(greeting())
print(details)
'''
'''
from modules import *
print(details)
print(greeting())'''

#Aliasing --> we use as keyword as shortcut for original file
'''
import modules as m
print(m.details)
'''
# we will work on some built-in modules --> random,math

import random
import time
#random modules --> get random number generation,random text
print(dir(random))
#OTP generation
#print(random.randint(1,10))
'''
for i in range(5):
    print(random.randint(1000,9999)) # start limit,endlimit
    time.sleep(5) #delays exection

print(random.random())#returns a float value of random
details = ['A long back','Once upon a time','Apatloo','Ten years ago']
print(random.choice(details))

#you can try story generation using choice
'''
#math module --> Mathematical constants,log,exp,trignometric

import math
#print(dir(math))
print(math.ceil(4.5)) # returns the next higest value
print(math.floor(4.78))
print(math.factorial(5))
print(math.pi)
print(math.gcd(5,3)) 
print(math.trunc(4.95))



