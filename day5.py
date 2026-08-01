'''
marks = int(input("Enter the marks (1-100:"))

if marks > 0 and marks <=100:
    if marks >= 90:
        print("user has secured grade A")
    if marks >= 80 and marks <= 89:
        print("user has secured grade B")
    if marks >= 70 and marks <= 79:
        print("user has secured grade C")
    if marks >=60 and marks <= 69:
        print("user has secured grade D")
    if marks < 60:
        print("user has failed,study again")
else:
    print("Enter only + ve values greater than 0 and less than 100")'''


#elif keyword --> if  elif

'''
marks =int(input("Enter the student marks:"))
if marks >=100:
    print("Entered values should be greater than 1 and less than 100")
if marks >= 90:
    print("user has secured grade A")
elif marks >= 80 and marks <= 89:
    print("user has secured grade B")
elif marks >= 70 and marks <= 79:
    print("user has secured grade C")
elif marks >=60 and marks <= 69:
    print("user has secured grade D")
elif marks < 60:
    print("user has failed,study again")
else:    
    print("no negative values")

age = int(input("Enter the age:"))
if age>=18 and age <=100:
    print('-----user has vote Eligibility -----')
    print('----- Access Granted -------')
elif age <18 and age >0:
    print('----- user still need to get vote eligibility ------')
    print('----- access need to wait for more',(18-age),'years(s)------')
else:
    print('----- only +ve values and less than 100 acceptable------')'''
          

#perfer if-else -else.....

a,b = 7,9
print(a)
print(b)
print(a,b)
name = "codegnan";batch = "DataAnalysis"
print(name,batch)
print(name,batch,sep=',')
print(name,batch,sep='------->')
#end '\n' ,\t -->tab space
print(name,batch,end='\t')
print(a,b,end='')
print("hyderabad")

name='codegnan';age=7;batch='DA-023';place='hyderabad'
#usage of commas
print(batch,'is in',name)
print(name,'is in',place,'age is',age,'years')
#old style formatting -->%d --> integer,%s-->string,%f-->float
salary = 24253.256
print("his salary is %d"%(salary))
print("his salary is %s"%(salary))
print("his salary is %f"%(salary))
print("his salary is %.1f"%(salary))

#.format() usage
print("{} is in {}".format(name,place))#order matters


#fstring usage (more recommended)

print(f'{name} is in {place}')
print(f'{"nithya"} is in {name}')


















































































