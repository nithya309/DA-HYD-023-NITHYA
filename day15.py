'''
sequences --> strings,lists,tuples,set,frozenset
mapping -->dictionary
'''
#set --> a set is a unique collection of objects,unordered,mutable,
#hashing,unindexed,unique,heterognous
#set(),{}
#a = {} it an empty dictionary
'''
a = set()
print(type(a))
stud_ids = {123,345,234,564,234}
print(stud_ids)
print(type(stud_ids))
print(len(stud_ids))
#print(stud_ids[2])#typrerror
print(234 in stud_ids)
#print(stud_ids *2) #type error
#print(stud_ids + stud_ids)#two sets cannot be merged
'''
'''
data = {12,3,4,5,(12,3,4),'nithya'}
print(data)#no lists inside a set (hashing technique)lists are mutable
print(len(data))
for i in data:
    print(i)
'''
'''
#methods on set --> add(),update(),remove(),discard(),pop()
names = {'nithya','mouni','sai','codegnan'}
print(len(names))
names.add('python')
print(names)
#names.add('nithya','poll')
#print(names)
names.add(('poll','police'))
print(names)
da_names = {'mani','akash','sai','sonu'}
names.update(da_names)
print(names)
print(da_names)
print(names)
print(len(names))
print(da_names)
print(len(da_names))
da_names.update(names)
print(len(names))
print(len(da_names))
'''
'''
#remove(),discard(),pop(),clear()
da_names = {'mani','akash','sai','sonu'}
da_names.remove('mani')
print(da_names)
da_names.discard('codegnan')
#discard() will remove an element an element if its present else it ignores
'''
'''
da_names = {'mani','akash','sai','sonu'}
da_names.pop()
print(da_names)
print(da_names.pop())
print(da_names)
da_names.clear()
print(da_names)
da_names.add('saira')
print(da_names)
da_names.update(['nithya','mouni'])
print(da_names)
'''
'''
#copy() #creates a shallow copy of set (independent of each other)
da_names = {'mani','akash','sai','sonu'}
d = da_names.copy()
print(d)
d.update({'python','java'})
print(d)
print(da_names)
'''

#mathematical operations --> union(),intersection(),difference()
#issubset(),issuperset(),isdisjoint()
'''
da_23 = {12,23,34,45,23,36}
da_24 = {34,46,47,23}
'''
'''
#event = da_23.union(da_24)
event = da_23 | da_24
print(event)
print(len(event))
#common = da_23.intersection(da_23)
print(common)
#print(len(common))
'''
'''
common = da_23.intersection_update(da_24)
print(common)# it returns none
print(da_23)
'''
'''
print(da_23)
print(da_24)
'''
'''
#difference() removes common element and prints rmng elements from frist
diff = da_23.difference(da_24)
print(diff)
f = da_23 - da_24
print(f)
'''
'''
symm = da_23.symmetric_difference(da_23)
#print(symm)
h = da_23 ^ da_24
#print(h)

da_24.remove(46)
da_24.remove(47)
print(da_24.issubset(da_23))
print(da_23.issuperset(da_24))
print(da_23.isdisjoint(da_24))
'''

n = int(input())
student_ids = input().split()
print(student_ids)
result = set(student_ids)
print(result)


































