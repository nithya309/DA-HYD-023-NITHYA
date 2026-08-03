
'''
marks = int(input("Enter marks:"))
if 0 <= marks <= 100:
    if marks >= 90:
        grade = "A"
        remark = "outstanding!"
    elif marks >= 80:
        grade ="B"
        remark ="Excellent!"
    elif marks >= 70:
        geade ="C"
        remark ="Good"
    elif marks >= 60: 
         grade ="D"
         remark ="Fair, needs improvement"
    elif marks >= 50:
        grade = "E"
        remark = "poor, needs serious improvement"
    else:
        grade ="F"
        remark ="Failed, needs to reappear"
    print("Grade:",grade)
    print("Remark:",remark)
    
else:
    print("Invalid marks entered")
'''


num = int(input("Enter a number:"))
if num==0:
    print("Zero is neither even or odd")
elif num %2 == 0:
    if num > 0:
        print("Even Number")
    else:
        print("Negative Even Number")
else:
     if num > 0:
         print("odd Number")
     else:
         print("Number odd Number")



month = int(input("Enter month number:"))
if month < 1 or month > 12:
    print("Invalid month entered")
elif month in [12,1,2]:
    print("Season:Winter")
elif month in [3,4,5]:
    print("Season: Spring")
elif month in [6,7,8]:
    print("Season:Summer")
else:
    print("Season: Autumn")





























































