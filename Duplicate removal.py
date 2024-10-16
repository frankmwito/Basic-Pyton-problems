# remove duplicates from a list

size_of_list = int(input("Enter the size of the list: "))
numbers_list = []

for i in range(size_of_list):
    number = int(input(f"Enter the values of list {i+1}: "))
    numbers_list.append(number)
    
sorted_list = sorted(numbers_list)

unique_list = list(set(sorted_list))

print(unique_list)