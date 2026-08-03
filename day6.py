'''
control statements --> control of flow of  execution of the program
--> conditional statements -->if,elif,else...
-->repetition statements (loops) --> for,while(for with else) (while with else)
-->jumping statements -->break,continue,pass

'''

#loops --> loops are helpful for repetition (Automative tasks)
#syntax for (for keyword):
#for keyword will be helpful to iterate over a sequence/range
'''

for <temp_var> in sequnce/range:
statement(s).....
......
'''
'''
#range(start,stop,step)
for i in range(10):
    print(i)'''
#in about case we got 10 iterations
for i in range(1,10):
    if i > 5 and i%2 ==0:'''
        print(f'value of i is -->{i}')'''
#npw i want to get only even number with about condition
'''
for i in range(-10,-1):
    print(i)
'''    
'''
#print -`10to -1
for i in range(-10,0,1):
    print(i)
'''
'''
#[] --> we generally Lists
names =['nithya','nikki','afeern']
for name in names:# len(obj)-->returns the number of items in a container
   # print(name)
   # print(f'Student Name is {name}')
   if name == "nithya":
       print(f"student name is {name}")
'''

# calculate the sum of first 10 number
#first understand your input --> range (11) -->10 number
#second understand your output --> sum (number)
#third we need to map tne  logic
'''
result = 0 #target variable
for i in range(21):
    if i %2 ==0:
        print(i)
        result = result + i #result += i
        print(result)
print(f' sum of 10 even number is {result}') '''


#understand the loops usage with Fitness streak example
#work_out -->1,work_out_missed-->0

'''
work_log =[0,1,1,1,0,1,0]
#result variable --> longest_streak
longest_streak = 0
current_streak = 0
for day in work_log:
    if day == 1:
       # print(day)
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = current_streak
    else: 
           current_streak = 0 #streak breaks
print(longest_streak)'''

































    
    







































