'''
identity operators -->checks the  identity of an object -->id()
#is,is not
'''
'''
a = 5
b = a
print(id(a))
print(id(b))
c = 5
print(id(c))
print(a is c)
print(5 == 5)
'''
'''
a = [1,3,5,6]
b = a
print(id(a))
print(id(b))
c = [1,3,5,6]
print(id(c))
#as we have lists (mutable collection) both  c and a lists will have different
#ids whereas values are same
print(c is a)#values are same
print(c == a) #output true
print(a is not c)'''

#Bitwise operators --> we perform bitwise operations over operands
#&(and),|(or).^(xor),shifting operators(<<,>>)
#Number will be converted to binary format

'''
print(5&3)# both 5 and 3 to be converted binary and bitwise and is performed

print(5|3)#bitwise or

print(5^3)#bitwise xor

print(5 and 3) #here and is  logical  operator check for both existances
#returns 5 in about case


print(5 or 3)#returns 3 in this case
'''
'''
#Leftship operator <<,Right shift operator >>





print(5 < 1) #false comparision
print(5 << 1)#left shift operation by 1 position
print(5 > 1)
print(5 >> 1) #right shift operation
'''
'''
print(15 << 2)# convert 15 to binary and perform 2 times left shifting

print(15 >> 2)# same 2 times right shifting'''

'''
# input formatting  --> input(),int(input()),float(input)))
#you know --> single input
#2 or 3 input --> map()
#group ofintegers -->list (map(int,input().split(','))

names =input("Enter the name:").split(',')
print(names)

name1,name2=map(str,input("Enter the friends name:").split(','))
print(name1,name2)'''

'''
#conditional statement -->if usage

syntax :

    if <condition>:
        statement(s)....
        .....
'''
'''
age = int(input("Enter the age:"))
if age >=18:
    print('your age is:',age)'''

'''
age = int(input("Enter the age:"))
if age>=18 and age in [19,21,20]:
    print('your age is',age)
    print(age)

#else keyword --> if-else
    
else
if-else usage as below
if <condition>:
statement(s):
statement(s)...
.....
else
statement(s)...
...
'''

#vote Elibility ->to check his\her voter eligibilty  and give access..
'''
age = int(input("Enter the age:"))
if age>18:

    print("you have voter eligibility and age is",age)
    print("Access Granted")

else:
    
    age = 18-age
    print("you dont have eligibility as your age is",age,"your")
    print("you need to wait  for more",age,"your")'''


marks = int(input("Enter student marks: "))

if marks > 0:
    if marks >= 90:
        print("Grade A")
    else:
        if marks >= 80:
            print("Grade B")
        else:
            if marks >= 70:
                print("Grade C")
            else:
                if marks >= 60:
                    print("Grade D")
                else:
                    if marks >= 50:
                        print("Grade E")
                    else:
                        print("Fail")
else:
    print("Invalid Marks")




















































































id
















    
