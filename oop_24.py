'''
oop --> Class,object,methods (__init__())
Encapsulation -->public,protected,private
Inheritance --> it is one of key feature of oop where we inheritance
class(base class(parent class))-->dervied class (child class)
whatsapp -->personal user,business user(catalog)community add
features -->code reusability,avoiding code dupilcation,
code maintainability,polymorphism (method overriding,(super()),method overloading,operator overloading__add__,__str__)

types : single inheritance (finger print)
--> one child class inherting properties from one parent class
multiple inhertance (mother,father-->child) -->one chald
class inheriting properties from two parent classes
multilevel inheritance (grandparent --> parent-->child)
level by levle
Hierarchical inheritance --> multiple child classes
inheriting propweties from single parent
hybrid inheritance -->it can carry one or more types of inheritance
syntax:
single inheritance:
class baseclass:
    statement(s)..
    ......
class derivedclass(baseclass):
    ........
    .......
'''

#whatsapp scenario -->personal user,Business user
'''
class User:
    """Single Inheritance usage"""
    def send_message(self):
        print('Sending Message')
    def voice_call(self):
        print('Making Voice Calls')
    def video_call(self):
        print("making video calls")
class BusinessUser(User):
   # pass
   def create_catalog(self):
    print("Displaying Products Catalog")
u1 = BusinessUser()
print(dir(u1))
u1.send_message()
u1.video_call()
u1.voice_call()
u1.create_catalog() 
'''
''' 
#social media login --> users -->update_users
class Users:
    """Single Inheritance usage"""
    company = "Codegnan"
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def full_name(self):
        return self.fname + self.lname
#u1 = Users("nithya","pothula")
#print(u1.full_name())
#print(u1.company) 
class Update_users(Users):
    def update_name(self):
        return self.fname.title()+" "+self.lnametitle().strip()
u1 = Update_users("nithya"" pothula")
print(u1.company)
print(u1.full_name())
print(u1.update_name())
u2 = Users("mounika","kala")
print(u2.full_name())
print(u2.company)
'''
#What if we have constructor in child class also....
#father --> kid (property)
'''
class Father:
    """Usage of Constructor in Single Inheritance"""
    def __init__(self):
        self.property = 1000000
    def father_property(self):
        print(f'Father Property is {self.property}')
#class kid(Father):
    #pass
class kid(Father):
    """Now childclass will have Constructor"""
    def __init__(self):
        #self.property = 200000
        self.cash = 2000000
    def kid_property(self):
        print(f'kid property is {self.cash}')
obj = kid()
obj.father_property()
obj.kid_property()
'''
#parent class is constructor overriding super()
#super()__init__()
# super()__init__(args)
# super() method() method overriding
class Father:
    """Usage of Constructor in Single Inheritance"""
    def __init__(self):
        self.property = 1000000
    def father_property(self):
        print(f'Father Property is {self.property}')
#class kid(Father):
    #pass
class kid(Father):
    """Now childclass will have Constructor"""
    def __init__(self):
        super().__init__() #calling superclass constructor
        self.cash = 2000000
    def kid_property(self):
        print(f'kid property is {self.cash}')
        print(f'Kid Final Property is{self.cash + self.property}')
obj = kid()
obj.father_property()
obj.kid_property() 

