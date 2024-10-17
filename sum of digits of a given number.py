# sum of digits of a given number

n = int(input("Enter the size of list: "))
num_list = []

for i in range(n):
    num = int(input(f"Enter the number {i+1}: "))
    num_list.append(num)
    
sum_of_digits = sum(num_list)

print(sum_of_digits)