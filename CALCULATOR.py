def add(a,b):
    return a+b


def sub(a,b):
    return a-b

 
def multiply(a,b):
    return a*b
def divide(a, b):
    return a / b


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while (1):
    
    choice = input("So what operation do you want to perform(1/2/3/4): ")
   
    if choice in ('1', '2', '3', '4'):
        try:
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number")
            continue

        if choice == '1':
            print(n1, "+", n2, "=", add(n1, n2))

        elif choice == '2':
            print(n1, "-", n2, "=", sub(n1, n2))

        elif choice == '3':
            print(n1, "*", n2, "=", multiply(n1, n2))

        elif choice == '4':
            print(n1, "/", n2, "=", divide(n1, n2))
        
        
        next_calculation = input("Do you want more calculations? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")