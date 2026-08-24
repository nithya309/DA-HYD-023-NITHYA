'''
object oriented programming is a mechanism or a process which revolves around creating objects it consists of teo important properties
Attributes --> variables which carry the data to the class
Methods-->methods is a function defined inside a class which carry the behavior of the object
the main features of oop --> Modularity,scalability,Encapsulation(binding the data (attributes),
Abstraction -->show only relevant informations to the class
Inheritance-->Acquring properties (attributes,methods)
Single -->Fingerprint
Multiple --> perents(mother,father) -->child
Multilevel -->Grandparent -->parent -->child
polymorphism --> methods over loading,methods overriding
operator overriding
syntax:
oop --> object oriented programming -->objects
'''
#Syntax for class creation:
'''
class Class Name:
    """Doc String"""
    attributes (characteristics)
    ..........
    def func(self): (behaviour)
        .....
        .....
     ......
obj = Class_Name()
'''
'''
#-->Student Class with basic details
class Student:
    """Understanding the usage of oop"""
    name = input("Enter the name:")
    id = input("Enter the id no:")
    gender = input ("Enter the gender:")
    email_id = input("Enter the mail_id:")
    #methods(behavior of the attributes)
    def display(self):
        print(f'Student Name is {self.name}')
        print(f'Student id is{self.id}')
        print(f'Student gender is {self.gender}')
        print(f'Student email_id is{self.email_id}') 
u1 = Student()
u1.display()
u2 = Student()
u2.display()
print(u1.__dict__) 
print(u2.__dict__)
'''
class Student:
    """Understanding the usage of oop"""
    def data(self,name,id,gender,email_id):
        self.name = name
        self.id = id
        self.gender = gender
        self.email_id = email_id
    #methods(behavior of the attributes)
    def display(self):
        print(f'Student Name is {self.name}')
        print(f'Student id is{self.id}')
        print(f'Student gender is {self.gender}')
        print(f'Student email_id is{self.email_id}') 
u1 = Student()
u1.data('nithya','CGH2341','female','nithyapothula8341@gmail.com')
u1.display()
print(u1.__dict__)
#Create a class with Car Brand name,price,color -->display
            
        