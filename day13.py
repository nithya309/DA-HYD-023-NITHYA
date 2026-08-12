'''
sequences -->strings,lists,tuples,set
mapping -->dictionary
'''

#Lists --> collection of heterogenous elements(items)
#Lists -->indexed,ordered,mutable,heterogenous,we use [] to store the data
'''
marks = [35,25,21,45]
print(marks)
print(len(marks))
print(type(marks))
'''
#operations : indexing,slicing,striding,membership,merging,repetition

#Nested Lists --> A list inside another list
'''
names = ['Codegnan',25,4.6,[45,35,25,65],'DA23',34]
print(len(names))
print(names[0])
print(names[3])
print(names[-3])
print(type(names[0]))
print(names[0][:4])
print(names[0][4:])
#get the output as cdga
print(names[0][::2])
names[0] = names[0][::-1]
print(names)
'''
'''
names = ['Codegnan',25,4.6,[45,35,25,65],'DA23',34]
print(names[3])
print(len(names[3]))
print(names[3][2])
#indexing,slicing -->mutable
names[2] = 'python'
print(names)
#by indexing in we change the elements,length of collection will remain same
names[4] = ['codegnan','PFS','JFS','AA','DA']
print(names)
print(len(names))
print(names[4][0][4:])
'''
'''
names = ['Codegnan',25,4.6,[45,35,25,65],'DA23',34]
names[3:4] = ['nithya','sai','mouni','thanu']
print(names)
#in slicing whatever elements u pass as per the logic length keeps on incre 
print[3:6:2] = ('python','java')
print(namrs)


#task--->create a nested list with strings, lists and work on indxing,slicing,striding
#added advantage if u could add string functions also to it


#lists functions --> append(),insert(),extend(),pop(),remove(),clear()
#index(),count(),copy(),sort(),reverse()
'''
'''
names = ['Codegnan',25,4.6,[45,35,25,65],'DA23',34]

names = ['codegnan','nithya']
names.append('data')
print(names)
names.append(['anaiysis', 'agents'])
print(names)
print(names[3].append('chatgpt'))#it returns none as append is applicable
#on lists not print
print(names[3])
'''      
#extend() -->inserts multiple elements to the end of list
'''
names.extend('analysis')
print(names)
names.extend(['analysis'])
print(names)
names.extend([45,75,24,56])
print(names)
#names.extend(35,45) typeerror
#print(names)
'''
'''
#insert(index,object) --> inserts given objct before index 
names = ['Codegnan',25,4.6,[45,35,25,65],'DA23',34]
names.insert(1,'python')
print(names)
names.insert(0,'java')
print(names)
names.insert(-1,'AAA')
print(names)
'''
#pop(),remove(),clear()
#pop(),by default last,else given index
names=['codegnan', 'nithya', 'data', ['anaiysis', 'agents']]
print(names.pop())
print(names)
names.pop(2)
print(names)

#remove() we can remove a specific value
names.extend([23,14,15])
print(names)

names.remove(14)
print(names)
#names. remove(14) #it raises valueError
del names[1:3] #del keyword will apply permanent changes
print(names)
names.clear()
print(names)
task-->#data =['codegnan','saketh','python','java']#input
#output should be as follows
'''
0 : codegnan
1 : saketh
2 : python
3 : java













