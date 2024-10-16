# prime number check

def prime_number(num):
    if num > 1:
       for i in range(2, num):
           if num % i == 0:
               return False
           else:
               return True
    else:
        print("Number must be greater than 1")
        return False
    

print(prime_number(int(input("Enter any number to check if its a prime number: "))))