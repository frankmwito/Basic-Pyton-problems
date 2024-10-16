# sum of even numbers

list_of_integers = []
num_of_integers = int(input("Enter the maximum number of integers: "))

for i in range(num_of_integers):
    integer = int(input(f"Enter any integer @ {i+1}: "))
    list_of_integers.append(integer)
print(f"The new list of integers i: {list_of_integers}")

for num in list_of_integers:
    if num % 2 == 0:
        sum = 0
        sum += num
        print(f"sum of even number is: {sum}")
    else:
        print(f"{num} is an odd number")
        
        