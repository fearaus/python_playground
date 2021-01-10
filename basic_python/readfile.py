#old style
myfile = open("fruits.txt")
print(myfile.read())
myfile.close()

#better styl e, with autoclose resource
with open("fruits.txt") as myfile:
    content = myfile.read()

print(content)


#write file
with open("vegetables.txt","w") as newFile:
    newFile.write("tomato")