x= [23, 34, 33]
#n = input("Enter list value")
#x.append(n)
if all([i%2 == 1 for i in x]):
    print("True")
else:
    print("False")

x = [ i for i in enumerate(x[::-1])]
print(x)
#n= [ i,v for i,v in x]
ddd = dict()
for i,v in x:
    ddd[i] = v

n = [ (v,i) for i,v in ddd.items()]
print(n)
