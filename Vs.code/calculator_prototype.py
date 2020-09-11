print("Calculator")

while True:
    while True:
        n1 = input("First_number: ")
        operator= input("Operator: ")
        n2 = input("Second_number: ")
        try:
            n1 = float(n1)
            n2 = float(n2)
            break
        except:
            print("invalid input. Retry again...")
    if operator == '+':
        result = n1 + n2
    elif operator == '-':
        result = n1 - n2
    elif operator == '*':
        result = n1 * n2
    elif operator == '/':
        result = n1 / n2
    else:
        result = "No result!!!" 
        print("Invalid input")
        
    print("Result",result)
    print("Again....")
    