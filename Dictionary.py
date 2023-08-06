#Dictionary
info = {"Name":"Nisha","Roll":12,"Name2":"Garima"} #"Name" is Key and "Nisha" is its value, keys are immutable type and values can be changed(mutable).
print(info)
info["Class"]="ABC"
info["Name2"]="qwe"

for i in info:
    print(i ,info[i]) # Traversal