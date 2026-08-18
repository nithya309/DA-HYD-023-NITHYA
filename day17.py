'''
Tokens,Datatypes --> control Flow statement --> if,elif,else,for,while,break
continue..

procedure oriented programming

Functions -->A function is a block of code which performs a specific task
its a reusable group of statements where we define using
def keyword
Advantages --> code reusability,code maintainability,ease of debuggin,
avoiding code duplication,modularity

syntax -->
def fname(parameters):
"""Doc String"""
statement(S)........
...........
return value(S).....
fname(args) function call
'''
#to perform sum of given objects
'''
def add (a,b):
    """Sum of objects"""
    c = a+b
    return c
print(add(12,3)) #Addition
print(add('code','gnan')) #concatenation
print(add([12,5],[12,34]))#merging
c,d = map(int,input("Enter the values:").split(','))
print(c,d)
print(add(c,d))
'''
'''
def add(a,b):
    """Sum of objects without return"""
    print(a+b)
add('code','gnan')
print(add(12,-34)) #it returns result along with None
'''
'''
name,age,salary = "Nithya",22,45000
#usage of return

def details():
    #return name,age,salary
    #return "codegnan"
    return 23+35+45
   print(details())
'''
'''
#There are 5 types of arguments:
    
-->positional arguments
-->default arguments
-->keyword arguments
-->variable length arguments(*args)
-->keyword variable length argument(**kwargs)
'''
#positional arguments --> number of arguments in function defn should
 #match with function call (order has to be maintained)
'''
def details(name,place):
    """To store the details"""
   # name = "Codegnan"
   # place = "Hyderabad"
    #return name,place
   print(f'Name is {Name}')
   print(f'Place is {place}')
#print(details("Nithya","Codegnan"))
#print(details("Sai","Vizag"))
c,d = map(str,input("Enter the values").split(','))
details(c,d)
'''

#Default arguments -->we can make arguments as default but not first arguments
#as default
'''
#def grocery(item="cheese",price = 100):
def grocery(item ="Burger",price):
    """usage of default arguments"""
    print(f'The Item is {item} and price is {price}')

grocery("Milk",32)
#grocery(32,"MILK")
grocery("Bread")
grocery()
'''
'''
#keyword arguments --> whenever we want to specify the name of argument
def employee(name,salary,role):
    """Keyword arguments usage"""
    print(f'Employee name is {name},role is {role} and salary is {salary}')
employee("sai",20000,"Admin")
employee(salary = 25000,role="Frontdesk",name="Asha")          
'''




