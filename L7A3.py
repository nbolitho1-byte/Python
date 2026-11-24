ride=int(input("Please enter whether you would like to ride a bike or scooter. Bike=1 Scooter=2: "))

if ride==1:
    bike=int(input("Please enter whether you would like an electric mountain bike or a dirtbike. 1=Mountain Bike and 2=Dirtbike"))
    if bike==1:
        print("You have selected a mountain bike!!!")
    else:
        print("You have selected a dirtbike!!!")

elif ride==2:
    scooter=int(input("Please enter whether you would like an electric scooter or a skate scooter. 1=E-Scooter and 2=Skate scooter"))
    if scooter==1:
        print("You have selected a E-SCooter!!!")
    else:
        print("You have selected a Skate Scooter!!!")
else:
    print("You haven't entered an option")
