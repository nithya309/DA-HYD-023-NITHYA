'''
polymorphism -->it is also of one key feature of oop,
poly --> many
morph -->forms
methods with same name can take different parameters(args)
-->method overloding(compile time polymorphism)
--> method overriding(run time)
--> operator over loading(+,*)(__add__,__str__)
horstar -> free user --> can watch the movies with advertisements
premium user --> can watch premium content without advertisements
vip user --> live content,streaming quality,premium content 
'''
#method over loading :
'''
class HotStar:
    """Understand polymorphism"""
    def watch():
        print(f'User logged into Hotstar...opening home page')
    def watch(self,movie):
        self.movie = movie
        print(f'User watching {self.movie}')
app = HotStar()
app.watch("leo")
#app.watch() it returns error as watch() is overloaded 
'''

#1)method usage with default arguments
#2)method usage with variable length arguments (*args)
#3)mothod usage with type of arguments
'''
class Hotstar:
    """Method usage with defiult argument"""
    def watch(self,movie=None):
        if movie is None:
            print(f'User logged into Hotstar...checking..')
        else:
            self.movie = movie
            print(f'User started watching {self.movie}')
app = Hotstar()
app.watch()
app.watch("vikram")
''' 
'''               
class Hotstar:
    """Method usage with defiult argument"""
    def add_watchlist(self,*movies):
        print(movies)
        for movie in movies:
            self.movie = movie
            print(f'User watching {self.movie}')
app = Hotstar()
app.add_watchlist()
app.add_watchlist('Loe','vikram','kgf')

#method over loading with type of arguments args
'''
'''

class HotStar:
    """Method over loading with type of arguments usage"""
    def watch(self,content):
        if isinstance(content,str):
            print(f'User watching {content}')
        elif isinstance(content,list):
            print('playing playlist')
            for movie in content:
                print(movie)
app=HotStar()
app.watch("arya")
app.watch(['arya','kgf','arya2'])
'''

#method overriding
# it happens in the scenario of inheritance ,where if child class is
#having method

class Freeuser:
    """Understanding method overriding"""
    def watch(self):
        print("User logged into Homepage....")
class PremimUser(Freeuser):
    """Using Inheritance"""
    def watch(self,movie):
        self.movie = movie
        print(f'User watching {self.movie}')
        super().watch()
obj = PremimUser()
obj.watch("kgf")
