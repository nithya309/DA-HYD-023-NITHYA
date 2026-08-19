'''
Functions -->variable length arguments (*args)
--> keyword

variable length arguments --> the number of poisitional arguments are not
we can pass any number  of argumunts ,but we need touse...
'''
'''
def sample(*args):
    """Simple demo for *args"""
    print(args)
    print(type(args))
sample()
sample(1,3,5,6)
sample('codegnan','nithya',23)
details = [24,45,35,65]
sample(details)
sample(*details)
'''
'''
a,b,c = 13,4,'da'
print(a,b,c)
#a,*b,c = 'python','codegnan',23,45,9.7,'data'
#a,*b,c = 'python','codegnan',23,45,9.7,'data'
a,b,*c = 34,'codegnan'
print(a)
print(b)
print(c)
c.extend([23,45,6,7])
print(c)
'''
'''
#Task --> we wanted to calculate the sum of given objects using function
def add(*a):
    """Sum of give objects"""
    print(a)
    print(type(a))
    #take output variable as result
    result = 0
    for i in a:
        #print(i)
        #if type(i) == int or type(i) == float:
        if type(i) in (int,float,complex):
            result = result + i
    return result
#print(add())
#print(add(12,3,4,5))
#print(add(3,4,5,'poll','dear',45,4.5))
b = list(map(int,input("Enter the value").split(',')))
#print(add(*b))
print(b)
print(*b)
for i in b:
    print(i,end=' ')
'''
#keyword variable length arguments --> we can pass any number of keyword
#arguments we use ** representation,data is stored in dictionary
'''
def details(**kwargs):

    """usage of **kwargs demo"""
    print(kwargs)
    print(type(kwargs))
details()    
#details(2,3,4,6) type Error
details(name="codegnan",place="hyd",batch="da")
details(ids=2345,age = 47)
batch = {'number':'da23','place':'hyd'}
details(**batch)
'''

#now let us include both of them into a function
def sample(*a,**b):
    """usage of both variable length and keyword variable length args"""
    result = 0
    for i in a:
        if type(i) in (int,float,complex):
            result = result + i
    #print(result)
     #return result       
    for key,value in b.items():
        print(f'key is {key}')
        print(f'value is {value}')
    return result    
print(sample(2,4,5,'police','codegnan',3.5,
       name="codegnan",
       place="hyd",
       batch="da23"))

#sample(name="codegnan",23,ids=23445) #positional args followa keyword args
















