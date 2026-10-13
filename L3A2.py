name="Noah"
age=13
height=150.8
student=True

print("My name is", name)
print("This data is type:", type(name))

print("My age is", age)
print("This data is type:", type(age))

print("My height is", height)
print("This data is type:", type(height))

print("I am a student, this is: ", student)
print("This data is type:", type(student))

print("After typecasting: ")
age=str(age)
height=int(height)
print(age)
print("The updated data type is: ", type(age))
print(height)
print("The updated data type is: ", type(height))