for i in range(4, 13, 2):
    print(i)
code= input("Enter the code: ")
try:
    code = int(code)
except:
    print("You enter invalid code!")
    quit()
print("You sucessfully enter the code")
x= list(range(10,20))
print("Keep the following code:", x)