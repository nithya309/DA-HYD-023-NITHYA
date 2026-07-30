'''
age = float(input('Enter the age:'))
print(age)
print(type(age))
'''
'''
name = input("Enter the name:")
print(name)
print(type(name))
'''
'''
marks = int(input("Enter the marks:"))
print(marks)
'''
'''
a = input().split()
print(a)
'''
'''
a = input() .split()
print(a)
'''
'''
a = input("Enter the values:").split(',')
print(a)'''
'''
#list of integers
marks = list(map(int,input("Enter the values").split(',')))
print(marks)
'''
'''
#Now we want to accept 2 values from user
age,salary = map(int,input("Enter the values").split(','))
print(age)
print(salary)
'''

#single input --> int(input())
#two input --> a,b =map(int,input().split(',')
#any number result as list --> a = list(map(int,input().split(',')))
'''
marks = list(map(float,input("Enter the values").split(',')))
print(marks)
'''

#Accepting input from user --> int,float  -> input formatting

#operators --> operators perform operations between values(operands)

#Arithemetic operators
'''
print(5+3)
print(5-3)
print(5*3)
print(5/3)
print(5//3)#float
print(5%3)#divisible
#floor division (interger division)-->returns quotient

#power (exponential)
print(5**3)

#Task --> Accept integer input as length,breadth --> find the area of rectangle
#Area = length *breadth
'''
'''
length=int(input('Enter the value:'))
breadth=int(input('Enter the value:'))
Area=length*breadth
print(Area)
'''
'''
#Assignment operators -->assign the values
# = , +=,-=
a = 45
print(a)
#update the value of a
a = a + 5 #a+=5
print(a)
b = 35
b +=a #b =b +a
print(b)
b -=5 #b =b-5
print(b)

'''
#Task : *=,/=,//=,%=,**=

a=25
print(a)
a *=5

age = 25
print(age ==25) #returns boolean output
print(age !=35)
print(age < 25)
print(age <=25)
print(age >35)
print(age>=35)

print(-5 <-1)

#membership operators -->in,not in -->boolean
#it check for the existance of an object in a collection

marks = [56,75,45,85]
print(35 in marks)

#print(35 in 355)#TypeError

print(25 not in marks)


#logical operators --> logical decision making --> and ,or,not
#and -->all condition to be satisfied
#or -->any one condition to be satisfied

'''
a = (25 in [25,45,65,]) and 45 < 56
print(a)
b = 45> 56 or  25 <=45
print(b)
c = not(True)
print(c)
'''
'''
#Identity operators --> check for identify of  an object -->id()
#is ,is not
a = 35
b = 35
print(id(a))
print(id(b))
print(a is b)
c = a
print(id(c))
print(c is a)
'''


a = [1,3,4,5]
print(id(a))
c = a
print(id(c))
print(c is a)
b = [1,3,4,2,5]
print(id(b))






















































































































































