'''
class Father:
    """Usage of Constructor in Single Inheritance"""
    def __init__(self,property):
        self.property = 1000000
    def father_property(self):
        print(f'Father Property is {self.property}')
#class kid(Father):
    #pass
class kid(Father):
    """Now childclass will have Constructor"""
    def __init__(self,cash,property):
        self.cash = cash
        super().__init__(property)
    def kid_property(self):
        print(f'kid property is {self.cash}')
        print(f'Kid Final Property is{self.cash + self.property}')
obj = kid(250000,1000000)
obj.kid_property()
obj.father_property() 
'''

#whatif child class is having same method name as
#parent class --> methods overriding
#area of square/rectangle
'''
class Rectangle:
    """Method Overriding usage"""
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def area(self):
        print(f'Area of Rectangle is {self.x*self.y}')
class Square(Rectangle):
    def __init__(self,x):
        self.x = x
    def area(self):
        print(f'Area of square is {self.x**2}')                
obj  = Square(7)
obj.area()
#obj.rarea() #attributeerror
'''
'''
class Square:
    """Method Overriding usage"""
    def __init__(self,x,y):
        self.x = x
        
    def area(self):
        print(f'Area of Square is {self.x**2}')
class Rectangle(Square):
    def __init__(self,x):
        self.y = y
        super().__init__(x)
    def area(self):
        super().area()
        print(f'Area of Rectangle is {self.x*self.y}')                
x,y = map(int,input("Enter the values:").split(','))
obj = Rectangle(x,y)
obj.area()
'''
#multiple inheritance
'''
class parent1:
    .......
class parent2:
    ......
class child(parent1,parent2):
    .......
'''

class User:
    """First Parent class with User features"""
    def voice_call(self):
        print('Making Voice Call')
class Notifications:
    def notification(self):
        print("Sending Notifications..")
class PremiumUser(User,Notifications):
    def verification_badge(self):
        print("Biue Tick Verification done")
user = PremiumUser()
user.verification_badge()
user.voice_call()
user.notification()                
'''
#Task1
class Device:
    def device_info(self):
        print("This is a Device")


class Laptop(Device):
    def laptop_info(self):
        print("This is a Laptop")


class Tablet(Device):
    def tablet_info(self):
        print("This is a Tablet")


class SmartDevice(Laptop, Tablet):
    def smart_info(self):
        print("This is a Smart Device")


obj = SmartDevice()

obj.device_info()
obj.laptop_info()
obj.tablet_info()
obj.smart_info()
'''

#Task2
class Vehicle:
    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")


class Bus(Vehicle):
    def travel(self):
        print("Bus is travelling")


obj1 = Car()
obj1.start()
obj1.drive()

obj2 = Bike()
obj2.start()
obj2.ride()

obj3 = Bus()
obj3.start()
obj3.travel()