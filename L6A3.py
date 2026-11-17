#BMI Checker
weight=float(input("Please enter your weight in kg"))
height=float(input("Please enter your height in cm"))

BMi=weight/(height/100)**2

print("Your BMI is",BMi)

if BMi <= 18.4:
    print("You are underweight.")
elif BMi <= 24.9:
    print("You are healthy.")
elif BMi <= 29.9:
    print("You are over weight.")
elif BMi <= 34.9:
    print("You are severely over weight.")
elif BMi <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")