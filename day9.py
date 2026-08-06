'''
sum=0
for i in range(1,5):
products=input('Enter product name:')
prices=int(input('Enter the price:'))'''
'''
products = list(map(int,input().split(',')))
total = 0
for i in products:
    total = total+i
print(total)
'''
'''
#Taks-->password
password=input("Enter password:")
upper=0
lower=0
digits=0
special=0
for ch in password:
    if 'A'<=ch<='Z':
        upper+=1
    elif 'a'<=ch<='z':
        lower+=1
    elif ch.isdigit():
         digits+=1
    else:
        special+=1
print(upper)
print(lower)
print(digits)
print(special)
'''
#task-->email
'''
email = input().split()
for mail in email:
    print(mail.split("@")[1])
'''


for i in range(1,6):
    movies=input('Enter movie name:')
    print(i,".",movies)










