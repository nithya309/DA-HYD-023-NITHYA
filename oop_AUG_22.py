'''
Constructor --> Instance methods -->Public Attributes
Encapsulation
'''
'''
class car:
    """Understanding the usage of Constructor in oop"""
    def __init__(self,name,brand,price,color):
        self.name = name
        self.brand = brand
        self.price = price
        self.color = color
    #methods(behavior)
    def display(self):
        print(f'car name is {self.name}')
        print(f'car brand is {self.brand}')
        print(f'car price is {self.price}')
        print(f'car color is {self.color}')
u1 = car ("Tata","Nexon","9Lakhs","Blue")
u1.display() 
'''
'''
class car:
    """Understanding the usage of Constructor in oop"""
    def __init__(self):
        self.name = "sedans"
        self.brand = "BMW"
        self.price = "50Lakhs"
        self.color = "White"
    #methods(behavior)
    def display(self):
        print(f'car name is {self.name}')
        print(f'car brand is {self.brand}')
        print(f'car price is {self.price}')
        print(f'car color is {self.color}')
u1 = car()
print(u1.name,u1.brand,u1.price,u1.color)
u1.display()
'''
#Encapsulation --> it is one of the main feature of oop
#it binds (bundles) the data (attributes) and the methods
#into a single unit (class) -->multipleobject
'''
class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,usersname):
        self.user = usersname
    def display(self):
        print(f'Student Username is {self.user}')
u1 = CodegnanPortal("nithya")
u1.display()
u1.user = "nithya"
u1.display()
print(u1.__dict__)
u2 = CodegnanPortal("mouni")
u2.display()
print(u2.__dict__)       
'''
'''
class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,usersname,_otp):
        self.user = usersname
        self._otp=_otp
    def display(self):
        print(f'Student Username is {self.user}')
        print(f'Student has received OTP as{self._otp}')
u1 = CodegnanPortal("nithya",2345)
u1.display()
u1._otp = 345
u1.display()        
'''
'''
class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,usersname,_otp,password):
        self.user = usersname
        self._otp=_otp
        self.__password = password
    def display(self):
        print(f'Student Username is {self.user}')
        print(f'Student has received OTP as{self._otp}')
       # print(f'Student password is{self.__password}')
u1 = CodegnanPortal("nithya",2345,"nithya8341")
print(u1.__dict__)
print(u1._CodegnanPortal__password)
'''
class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,usersname,_otp,password):
        self.user = usersname
        self._otp=_otp
        self.__password = password
    def get_password(self):
        #return"******"
        return self.__password
    def set_password(self,new_password):
        if len(new_password) > 6:
            print("wrong password not satisfied 6 characters")
        else:
            self.__password=new_password
            print("Now password is updated")
u1 = CodegnanPortal("nithya",2345,"nithya8341")
print(u1.get_password())
u1.set_password("nithya")
u1.set_password("nithya8341")
print(u1.get_password())


