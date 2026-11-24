#checking if child has illness so then they are automatically accepted
sick=input("Please enter if your child has a medical issue: (Y/N)").strip().upper()
#Programme for nested if-else
if sick=="Y":
    print("You have been accepted into the best SCHOOL EVERRRRR!!!")
else:
    atten=int(input("What is your attendance: "))
#checking for yattendance
    if atten >= 75:
        print("You have been accepted into the best SCHOOL EVERRRRR!!!")
    else:
        print("Sorry you have been DECLINED")