fname = open("Hasib.txt","w")
fname.write(input("Enter what you want to store in Hasib.txt:"))
fname.close
fname = open("Hasib.txt","r")
print(fname.read())
fname.close