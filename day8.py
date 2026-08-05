'''
tokens -->keywords, identifiers, literals,operators,punctuators,variables
operators --> numberic data (int,float,complex),bool
control flow -->if,elif, for,while
sequences -->strings,lists,sets,tuples,mapping(dict)
'''
#strings --> group of characters we use single or double or triple quotes
#for representation of strings..
#strings are  immutable,orderred,indexed collection
#space is also a character
'''
name = 'codegnan'
print(name)
print(type(name))
print(len(name))

#index() --> fetch the object (position) starts at 0 and ends at len(obj)-1
#we use [] represntation
print(name[0])
print(name[5])
#print(name[25])-->index error --> as its out of range

#negative indexing --> -1 to len(obj)
print(name[-1]) # it returns last character
print(name[-3])


#slicing--> we can access group of characters
#we use [start:end]#staet default --> 0, start is included,end is excluded

name = 'codegnan'
print(name[:])
print(name[0:])
print(name[:4])
print(name[1:5])
print(name[3:7])
print(name[:6])
'''

'''
name='python'
print(name[3:7])
print(name[7:3])
#slicing is applicable from lower index to higher index
print(name[:45])'''
'''
print(name[-1:-5])
print(name[-5:-1])
#print 'on' from above string
print(name[4:])
print(name[4:6])
print(name[-2:])'''
'''
print(name[1:-2])
print(name[2:-6])
#observe +ve,+ve,-ve-ve&+ve,-ve all possibilies
'''
#striding -->[strart:end:stop]
'''
course = 'DataAnalysis'
print(len(course))
print(course[:4])
print(course[4:])
print(course[-3:])

print(course[::3])
print(course[::2])
print(course[1:6:3])#[1:6] --> [1:6:3]-->aA

#tnys
print(course[2::3])
print(course[::-1])
print(course[::-2])
print(course[::-5])'''
'''
name = 'codegnan'
#name[3] = 'w' #string are immutable

#operations on strings --> indexing, concatenation repetition,membership
print(name * 3)
print('*' * 25)
#concatenation -> combining string
data = 'nithya' + 'python' +  ' ' + 'database'
print(data)
print('123' * 4)
print('code' in 'codegnan')

for i in 'codegnan':
    print(i,':')


for i in 'codegnan':
    print(i,end=' ')


name = "dataCodegnan"
#built-in functions
print(len(name))
print(min(name))
print(ord('A'))
print(ord('a'))
print(max(name))
print(chr(97))
print(sorted(name))#returns a list by sorting all elements
'''
'''
#methods on strings --> case-Conversions,finding/searching...
name = 'Codegnan data'
#case-conversions-->upper(),lower(),title(),capitalize()
a = name.upper()
print(a)
b = name.lower()
print(b)
#capitalize() --> converts frist letter to uppercase
c = name.capitalize()
print(c)
d = name.title()
print(d)
'''

#task A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#use loops and strings to return A-Z







