num1 = int(input("Enter the first number: \n "))
num2 = int(input("Enter the second number: \n "))
num3 = int(input("Enter the third number: \n "))


a = min(num1, num2, num3)
b = max(num1, num2, num3)
c = (num1 + num2 + num3) - a - b

print("The sorted Numbers order is \n ", a, c, b)
