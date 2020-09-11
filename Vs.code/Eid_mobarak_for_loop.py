for i in range(1998, 2021, 1):
    print("Eid Mobarak!!! [" + str(i) + "]")
number = [34, 34, 5345,23 ,23 ,2433, 342,23,]
largest = number[0]
count = 0
for i in number:
    count += 1
    if i > largest:
        largest = i
    print(largest, i)
print(largest , "Done and total iteration is:", count)
