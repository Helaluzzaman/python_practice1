smallest = None
largest = None
print(smallest, largest)
for i in [234, 23, 1, 23, 434,34,23, 43343, 343]:
    if smallest is None:
        smallest = i
    if largest is None:
        largest = i
    elif i > largest:
        largest = i
    elif i < smallest:
        smallest = i
    print(smallest, i, "||", largest, i)
    
print("Smallest:", smallest, "and largest", largest)