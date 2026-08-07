#task-->write a python program to calculate the
#innings of a batsman count the boundaries , dotbals ,total score using for
'''
list=[4,6,1,0,2,4,0,6]
total = 0
boundaries = 0
dotballs = 0

for i in list:
    total = total + i

    if i == 4 or i == 6:
        boundaries = boundaries + 1

    if i == 0:
        dotballs = dotballs + 1

print("Total Score =", total)
print("Boundaries =", boundaries)
print("Dot Balls =", dotballs)
'''
'''
#Task--->ATM
pin = "2612"
max_attempts = 4
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
'''

#task--->phone pattern
password = "159"
count = 0

while count < 3:
    user = input("Enter Pattern: ")

    if user == password:
        print("Unlocked")
        print("*     ")
        print("  *   ")
        print("    * ")
        break
    else:
        count += 1
        if count < 3:
            print("Wrong Pattern! Try Again.")
        else:
            print("Wrong Pattern!")
            print("Try again after 30 seconds.")
