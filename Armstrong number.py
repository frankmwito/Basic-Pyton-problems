# Armstrong number

def is_armstrong(n):
    armstrong = 0
    length = len(n)  # Length of the number (number of digits)
    
    for digit in n:
        armstrong += pow(int(digit), length)  # Add each digit raised to the power of the length
    
    if int(n) == armstrong:
        print("The given number is an Armstrong number.")
        return True
    else:
        print("The given number is not an Armstrong number.")
        return False
        
n = input("Enter the number: ")

print(is_armstrong(n))
