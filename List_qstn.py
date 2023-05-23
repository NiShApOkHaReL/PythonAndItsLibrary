std = ["Ram",10,"BEC","Bharatpur","Male",22]
print("Before changing")
print(std)
std[3] = "Ngt"
print("After changing:")
print(std)

print("Roll no: ",std[1])
print("Name: {} , Faculty: {} , Gender: {}".format(std[0],std[2],std[4]))
print(std[0:5:2])