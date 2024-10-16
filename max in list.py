# max number in a list

list_of_numbers = []
num_of_intergers = int(input("Enter the maximum number of integers: "))

for i in range(num_of_intergers):
    integers = int(input(f"Enter the {i+1} integer: "))
    list_of_numbers.append(integers)
 
max_value = max(list_of_numbers)

print(f"The maximum value int the list is: {max_value}")
