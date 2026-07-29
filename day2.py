'''
tokens--> variables,puncators

variables--> nNamed memory location,its a placholder for data
#rules are to be follwed
'''
#multiAssignment of variables

name,age,place='codegnan',7,'hyderabad'
print(name,age,place)
print(name,age,place,sep=' ,')
print(name,age,place,sep='-->')

#a,b=2,4,5 valueError as too value to unpack
#Reassigning vaeiables

name="codegnan"
a,b=45,1.5
print(a,b)
a,b=b,a
print(a,b,sep=',')
'''
a,b=b,c NameError as c is not defined
print(a,b)
'''

#deleting the variables-->del
#del a
#peint(a)
#del a,b
#print(a,b)

#punctuators --> [](lists),()(tuples),{}(dict,sets)
name="codegnan";age=7
print(name,age)

#Datatypes --> Numeric(int,float,complex),boolean,None,
# -->sequences -->Lists,Tuples,sets,strings,
# frozensets,mappings(Dict)

#loat datatype --> temp,salary,price
price=750.24;discount=2.5
print(price,discount)
print(type(price))

#complex -->combination of real and imag
i2 = 5
date = 5 + i2
print(date)

date =5+2j #j is imag representation
print(date)
print(type(date))

#Boolean --> True/False

valid = True
print(type(valid))

error = False
print(type(error))

#Typecasting -->int -->float,complex,bool

age=35
print(type(age))
b = float(age)
print(b)
c = complex(age)
print(c)
d = bool(age) #returns True for existing data
print(d)
e = bool(0)
print(e)

#float --> Typecasting
age=3.5
print(type(age))
b = float(age)
print(b)
c = complex(age)
print(c)
d = bool(age) #returns True for existing data
print(d)
e = bool(0)
print(e)

#complex --> Typecasting --> int,float,bool
data = 2+5j
print(type(data))
#b =int(data) #TypeError
#print(data)
#c = float(data)
#print(c)
d = bool(data)
print(d)
print(type(d))

e = int(float(bool(45)))
print(e)

f = 45 + 2.5 +2 + 3j +False
print(f)













































































#Numeric type -->int,fo
