# data type

name="sheshis" 
roll=4464
isActive=True


# if else

mark= 33


# Check grading conditions
if mark < 0 or mark > 100:
    print("Invalid mark! Please enter a value between 0 and 100.")
elif mark <= 33:
    print("Your grade is F")
elif mark <= 39:
    print("Your grade is D")
elif mark <= 49:
    print("Your grade is C")
elif mark <= 59:
    print("Your grade is B")
elif mark <= 69:
    print("Your grade is A-")
elif mark <= 79:
    print("Your grade is A")
else:
    print("Your grade is A+")
