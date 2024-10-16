# palindrome check

name = input("Enter your string of choice: ")

if name == name[::-1]:
    print(f"{name} is a palindrome")
else:
    print(f"{name} is not a palindrome")