print("Please enter 3 subjects that have the same max mark: ")

english=int(input("Marks obtained in English: "))
maths=int(input("Marks obtained in Maths: "))
science=int(input("Marks obtained in Science: "))

total_marks = maths + science + english

percentage = (total_marks / 300) * 100

print(percentage)
