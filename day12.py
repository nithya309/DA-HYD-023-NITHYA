'''
strings --> case conversions, searching &finding ,string testung methods,
replace,space removal
'''
'''
#searcging,finding, replacing,joining...
a = "Codegnan"
print(len(a))
print(min(a))
print(max(a))

b = a. index('g')#it return the index position
print(b)
c = a. index('n')#it return only the first occurance
print(c)
d = a. index('n',6)#it returns the next occurance
print(d)
#e = a. index('n',8)#valueError
#print(e)
#f = a. index('t')#valueError
#print(f)
g = a.index('n',2,6)
print(g)
'''

#index() --> returns last occurance
'''
a='Codegnan'
b = a. rindex('g')
print(b)
c = a. rindex('n')#here 'n' is occuring at 7th index
print(c)
#d = a. rindex('n',8)#it returns valueError
#print(d)
'''
'''
#count() -->returns the number of items object is repeating
a ='Codegnan'
print('Codegnan'.count('n'))
print('Code'.count('w'))#it returns 0 as we done have 'w' in 'code'
print('Nithyasree'.count('a'))
'''
'''
#find() -->first occurance but it avoid error returns -1 if substring is
#not found
print('codegnan'.find('r'))#it returns -1
print('codegnan'.find('n'))
print('codegnan'.rfind('n'))
'''
'''
a = "Data"
print(len(a))
for i in a:
    #print(i)
    print(a.count(i),a.index(i))
'''
'''
#Replacing,splitting,joining
#strings are immutable
a = 'Codegnan'
#a[4] = 's'
print(a.replace('g','s'))
print(a)
a = a.replace('g','s')
print(a)
'''
'''
a = 'code nithya python'
print(len(a))
b = a.split()#by default if we have space it splits
print(b)
print(len(b))
c = 'code,nithya,python'
d = c.split()
print(d)
e = c.split(',')
print(e)
'''
'''
#join(iterable)-->concatenate any number of strings
a='code'
b ='gnan'
print(a.join(b))
print(b.join(a))
print('#'.join('nithya'))
print(' '.join('nithya'))
'''

#string testing methods(boolean)
#isalpha(), isalnum(),isdigit(),isupper(),islower()......
'''
a = 'Codegnan123'
print(a.isalnum())#returns true for alphanumberic strings else flase
b = 'Codegnan'
print(b.isalnum())
print(a.isalpha())#returns true only for alphabets 
print(a.isdigit())#returns true only digits string
print('8341277207'.isdigit())
print('1234'.isnumeric())#this has upper edge (numbers,fractions,romans)
print('codegnan'.startswith('c'))
print('codegnan'.startswith('g',4))
print('codegnan'.endswith('f'))
'''
'''
print('codegnan'.islower())#returns true for all lowercase
print('COdegnan'.isupper())#returns true for all uppercase
print('Codegnan python'.istitle())
'''

#space removal --> strip() (removes leading and trailing spaces
'''
a = 'codegnan'
print(a.strip())
b = input("Enter the string:").strip().lower()
print(b)
'''
#zfill() filling with zeros as per the given numeric string
print('123'.zfill(4))
print('123'.zfill(7))

print('hai'.center(6))
print('hai'.center(6,'#'))
print('hai'.ljust(6,'#'))
print('hai'.rjust(6,'#'))












































