#Using NOT logical operator
a=12
b=10
c=10

print(not(a==b))

print(not(b==c))

#STRING
d="Skateboarding"
e="Mountain Biking"

if (not(d==e)):
    print(d,"is not the same as",e)

#Reversing the given condition
f=5
g=2
if not(f==2)==(g==2):
    print("Well done you passed the test!")

#Checking if number is not even
i=int(input("Please enter a number: "))

if not(i%2==0):
    print(i,"is an odd number")