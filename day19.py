'''
Functions --> arguments usage (variable length arguments)
-->keyword variable length arguments(**kwargs)

Exception Handling/scope of variables /Built-in functions

Exception handling --> it is a mechanism that helps to respond or make the
flow of execution in normal way,without this error will occur and disrup the
flow of program

common Exception --> Value Error, TypeError ,IndexError,AttributeError,
ZeroDivisionError....

syntax:

try:
#code that will cause the exception
except Exception as e:
        #code will catch the exception
finally:
        #runs irrespection of try/except...
        ....
'''
'''
#basic Exception handling
try:
    #a = 10
    a = int(input("Enter the value:"))
    result = 20/a
    #print(result)
#except Exception as e:
   # print(e)  # it returns the msg of error
except ValueError:
    print(f'Invalid entry enter only integer values')
except ZeroDivisionError:
    print(f'Division by zero is not possible')
except NameError:
    print(f'Check the name of variable properiy')

#Similarly if we want to check other Errors ->IndexError,AttributeError

try:
    a = [10,20,30]
    print(a[5])
#except Exception as e:
    #print(e)#returns the message of Error
except IndexError:
    print(f'Check the length of list properly and access elements')
except AttributeError:
    print(f'Dont rush write the name properly')
'''
'''
#handling exceptions at a time
try:
    a = [10,20,30]
    a.append(24)
    print(a[5])   
except (IndexError,AttributeError)as e:
    print(e)
    a = list(map(int,input("Enter").split(','))) # only for understanding
    print(a)
'''
'''
#BMI --> bmi = (weight) / (height)**2)
#Feet --> 12 inches --> 1 inch -> 2.54cm
while True:
    try:
        weight = int(input("Enter the weight in kgs:"))
        height = float(input("Enter the height in metres:"))
        #write my logical condition
        if weight > 0 and height > 0:
            break   #stops the flow of execution of program
            #continue   # skips the current iteration and proceed for rmng iterations 
            #print("bye")
        else:
            print("make sure to enter only correct values")
    except ValueError:
        print(f'make sure to enter weight as integer only,\
                height also as number')
bmi = ((weight) / (height)**2)
print(bmi)

#use exception handling along with jumping statement in
#Functions BMI task
'''

#Scope of variables --> scope is basically the region/area where it is
#accessible
#local scope global scope
#global keyword, encloseing scope(Nested Functions nonlocal keyword)

#Local scope --> variable defined inside the functions accessible inside
'''
def display():
    """Usage of Local Scope"""
    name = "Codegnan"
    print(name)
display()
#print(name)
'''
'''
#madifying global variable inside the functions and accessible outside the functions
count = 20
def data():
    """Usage of global keyword"""
    global count
    count = count + 5
    print(f'Value inside function is {count}')
data()
print(f'Value outside function is {count}')
'''
'''
#Local variable has high priority over global variable
count = 20
def data():
    """Priority of local vs global variable"""
    count = 5
    count = count + 5
    print(f'Value inside function is {count}')
data()
print(f'Value outside function is {count}')
'''
'''
#Encloseing Scope (nonlocal keyword)

def outer():
    """Outer function with local variable"""
    count = 5
    def inner():
        """Nested Function"""
        nonlocal count
        count = count + 10
        print(f'Value inside is {count}')
    inner()
    print(f'Value outside is {count}')
outer()    
'''
#Built-in functions --> variables Builtinscope
len = 56
print(len+4)
print(len('codegnan')) #type error

























