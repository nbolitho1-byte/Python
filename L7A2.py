units=int(input("Please enter the amount of electrical units used: "))

if units <50:
    amount=units*2
    surcharge=50
elif units <=100:
    amount=units*3
    surcharge=75
elif units <=200:
    amount=units*4
    surcharge=100
else:
    amount=units*5
    surcharge=200
final=amount+surcharge
print("The amount you have spent on electricity this year is: ",final)