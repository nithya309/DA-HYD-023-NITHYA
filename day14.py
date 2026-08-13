'''
Lists,Tuples..
'''
#List --> mutable,ordered, heterogenous

#index(),count(),copy(),sort(),reverse()
'''
details =['codegnan',7,2018,'Hyderabad']
print(len(details))
print(details.index(7))
print(details.index('codegnan'))
details.extend([7,21,45,21])
print(details.index(21))
print(details.index(21,6))
#print(details.index('python')
'''
'''
#copy() -->shallow copy of the give collection
data =['codegnan',7,2018,'Hyderabad']
new = data.copy()
print(new)
print(type(new))
print(len(data))

new[2] = 'Agentic AI'
print(new)
print(data)

data.append('Nithya')
print(data)
print(new)
data.pop()
print(data)
print(new)
'''
'''
data = [1,4,5,[21,34,45],23]
print(data)
new = data.copy()
print(new)

new[3][2] = 'Agents'
print(new)
print(data)

new[1] = 'Python'
print(new)
print(data)
'''
'''
marks = [14,24,-45,27,35]
print(marks)
#print(marks.sort())
#print(marks)
marks.sort(reverse = True)#returns in Descending order...
print(marks)
marks.insert(3,'code')
#marks.sort()
#reverse() --> returns in reverse order
marks.reverse()
print(marks)
print(marks[::-1])
'''

#type(),len(),max(),min(),print()
'''
print(sorted('codegnan'))#returns list in ascending order
#print(sorted['code','23',34,45]))#raises error
'''

#Tuple -->Tuple are indexed,ordered,heterognous,immutable collection
#dimensions,coordinates,database records,we prefer () for tuple
'''
a = ()
print(type(a))
print(len(a))

dimensions = 1.5,2.5
print(dimensions)
print(type(dimensions))
print(len(dimensions))

#operations --> indexing,slicing,striding,membership,merging,repetition

courses = ('PFS','JFS',('DA','DS'),'AgenticAI',[100,6,6])
print(courses)
print(len(courses))
print(courses[-1][2])
print(courses[2][-1])
print(courses[3][-2:])
#courses[2] = 23 Tuple are immutable
courses[-1].append('codegnan')# we can make any modifications inside list
print(courses)

#task-->create a nested tuple as above and work on sliciing,striding and list functions

print('PFS' in courses)#membership
d = courses * 2 #repetition
print(d)
e = courses + (2,3,4,5)#merging
print(e)
'''
'''
#Tuples immutable -->count(),index()
courses = ('PFS','JFS',('DA','DS'),'AgenticAI',[100,6,6])
print(courses.index('AgenticAI'))
print(courses.count('Agents'))

#print(courses.sort()) #AttributeError -->sort() is in lists not in tuples

print(sorted(courses[-1]))
#print(sorted(courses))#as we have mixed type

#typecasting
d = tuple(sorted((23,12,3,4,5)))
print(d)
'''
'''
#accept group of integers space separated
a,b = map(int,input("Enter the values").split())
print(a,b)
'''
print('9+4')
print(eval('9+4'))

a = eval(input("Enter a list:"))
print(a)
print(type(a))

#Task:Take a user input as string ,do this in two ways..
'''
1:gave the count of each repeating character
Test case 1: programming

r is repeating 2 times
g is repeating 2 times
m is repeatine 2 times
'''




























      










