# Factorial calculation

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(result)
        


factorial(int(input("Enter the number you wish to find the factorial: ")))