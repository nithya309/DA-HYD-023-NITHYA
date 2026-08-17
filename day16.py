'''
mapping --> dictionary --> collection of key-value pairs used to store
related data --> JSON,APIS,database records

dict() --> data = {}  -->data = {key : value}
dictionary is mutable indexed keys ordered heterogenous,
keys must be unique (int,strings,float values...)
'''
'''
details = {}
print(type(details))

details = {'ID':'CGH4022','Name': 'Nithya',
           'Gender':'F','Age':20,
           'Batch':'DA23', 'Place':'Hyd'}
print(details)
print(len(details))

#Access the data from dictionary
#details[0] # key Error

print(details.keys()) # it returns keys from the dictionary
print(details['ID'],details['Name'])
# if key name is not matching / invalid
#print(details['Marks']) #keyError as marks is not present
details['Marks'] = []
print(details)
print(type(details['Marks']))

details['Marks'].append(20)
print(details)
details['Marks'].extend([10,20,50,40])
print(details)

#create a key-value pair of practice session
details['practice session'] =('Tuesday','Thursday','Saturday')
print(details.keys())
# Accessing 3rd day marks of student  
print(details['Marks'][2])
#Accessing 2nd day of praction session
print(details['practice session'][1])
details['MI'] = ('Monday','Wednesday','Friday')

print('Wednesday' in details)
print('MI' in details)
'''
'''for i in details:
    print(i)
'''
'''
for i in details.keys():
    print(f'key = {i}')
    print(f'value = {details[i]}')
'''
'''
#keys() --> returns keys from the dictionary

for i in details.values():
    print(i)
'''
'''
for i in details.items():
    print(i)
'''
'''
for key,value in details.items():
    print(f'key is {key}')
    print(f'value is {value}')
'''
'''
#update()
details.update({'Marks':[],
                'practice session':('Tuesday','Thursday','Saturday')})
print(details)
details['Marks'].extend([25,30,25])
print(details)
Marks = list(map(int,input("Enter the Marks:").split(',')))
print(Marks)
details['Marks'].extend(Marks)
print(details)
'''

details = {'ID':'CGH4022','Name': 'Nithya',
           'Gender':'F','Age':20,
           'Batch':'DA23', 'Place':'Hyd'}

print(details.keys())
print(details.get('Name'))
print(details.get('Brach'))
print(details.keys())

details.setdefault('Branch','BSC')
print(details)
details['Branch'] = 'BCOM'
print(details)

print(details.setdefault('Name'))
print(details.keys())

print(details.pop('Branch'))
print(details.keys())

print(details.popitem())
print(details.popitem())
print(details.popitem())

del details['ID']
print(details.keys())

details.clear()
print(details)

#fromkeys()
data = ['Nithya','Sree','data']
b = dict.fromkeys(data)
print(b)
b['Nithya'] = 34
print(b)
c = dict.fromkeys(['CGH1234','CGH2344'],['code','gnan'])
print(c)


                                         
                                        













    













