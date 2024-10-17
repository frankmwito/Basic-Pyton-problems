# sort a dictionary by its value

my_dict = {}

size_of_dict = int(input("Enter the size of the dictionary: "))

# Collecting dictionary entries
for i in range(size_of_dict):
    name = input(f"Enter the person's name @ {i+1}: ")
    age = int(input(f"Enter the age of person @ {i+1}: "))
    my_dict[name] = age

# Sorting the dictionary by values
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Printing the sorted dictionary
print("Dictionary sorted by values:")
for name, age in sorted_dict.items():
    print(f"{name}: {age}")

    