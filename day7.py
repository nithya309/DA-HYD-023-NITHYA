
'''
#usage of else with for--> the else keyword will only be
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
            print(f'Longest_streak is {longest_streak}')
            break
    else:
        current_streak = 0
else:
    print(f'longest_streak is{longest_streak}')
print("Execution done")
'''

 
'''
#for notification in notification:
#try to take notifications from user --> list of integers
notifications = list(map(int,input("Enter the values --> 0 or 1:").split(',')))
print(notifications)
for notification in notifications:
    if notification == 1:
       print('Unread Notification')
else:
    print('All caught Up')'''

'''
while True:
    print("Yes")
'''


#It runs an infinite loop we need to press ctrl+c(keyword interrupt)
'''
i = 0
while i<=10:
    print(10-i)
    i=i+1# counter
'''

# banking scenario --> PIN authentication if more than 3 attempts
#Account locked..

pin = "2612"
max_attempts = 3
current_attempt = 0
while current_attempt <= max_attempts:
    entered_pin = input("Enter the ATM PIN:")
    if entered_pin ==pin:
        print("login successful")
        break
    #continue #it hold for this condition
    else:
        print("Entered PIN is wrong..Try again carefully")
        current_attempt +=1
else:
    print("Account Locked,try after 24hours...")


































































