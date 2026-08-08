#Task-->
'''
correct_code = "159"

while True:
    code = input("Enter secret code: ")

    if code == correct_code:
        print("Correct")
        break
    else:
        print("Wrong")

'''
#Task-->otp verification
'''
otp = "1234"
attempt = 0

while attempt < 7:
    code = input("Enter OTP: ")

    if code == otp:
        print("Correct OTP")
        break
    else:
        print("Wrong OTP")

    attempt = attempt + 1

if attempt == 7:
    print("OTP Expired")
'''
'''
#Task-->food order
count = 0
while True:
    food = input("Enter food: ")
    if food == "exit":
        print("Thank you for ordering!")
        print("Total orders:", count)
        break
    print(food, "added to order")
    count = count + 1
'''

#Task-->
secret = 'python'
attempt = 0
while attempt < 3:
    game = input('Enter the game name: ')
    if game == secret:
        print("You win the game")
        break
    else:
        print("Try again...")
        attempt += 1
else:
    # This executes ONLY if the loop finishes without hitting a 'break'
    print("You lost the game")
    
        































