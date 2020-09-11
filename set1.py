a = {1,2,3,4,5,5, 6,7}
b = {3, 4, 5, 6, 7, 8, 9,10}

print("a =",a, "          ","b =", b)
print("difference double:", a^b)
print("difference a-b :", a-b)
print("difference b-a :", b-a)
print("union:", b|a)
print("intersection: ", b&a)
b.add(34)
print("after add", b)
b.pop()
print("pop of b", b)
b.add("Hasib")
print(b)
import itertools
print(dir (itertools))
for i in itertools.count(1):
    print(i)
    if i == 111:break
count = 0
for i in itertools.repeat(b):
    print(i, count)
    count += 1
    if count == 111:break
count = 0
for i in itertools.cycle(b):
    print(i, count)
    count += 1
    if count == 111:break
    
lst = list(itertools.cycle(b))