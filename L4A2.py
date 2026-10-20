withdrawal=int(input("Please enter the amount you would like to withdraw: "))

note1=withdrawal//100
note2=(withdrawal%100)//50
note3=((withdrawal%100)%50)//10

print("Notes of 100 rupees is",note1)
print("Notes of 50 rupees is",note2)
print("Notes of 10 rupees is",note3)