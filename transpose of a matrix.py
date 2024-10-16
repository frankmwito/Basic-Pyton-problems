# transpose of a matrix

size_of_list = int(input("Enter the size of a single list in a matrix: "))

l1 = []
l2 = []
l3 = []

for i in range(size_of_list):
    integers_1 = int(input(f"Enter the value of list1 in {i+1}: "))
    l1.append(integers_1)
    integers_2 = int(input(f"Enter the value of list2 in {i+1}: "))
    l2.append(integers_2)
    integers_3 = int(input(f"Enter the value of list3 in {i+1}: "))
    l3.append(integers_3)
    
major_list = [l1, l2, l3]

print(f"Original Matrix:",major_list )

for row in major_list:
    print(row)

transposed_matrix = []

for row in range(len(major_list[0])):
    new_row = []
    for column in range(len(major_list)):
        new_row.append(major_list[column][row])
    transposed_matrix.append(new_row)
    
print("Transposed Matrix:")
for row in transposed_matrix:
    print(row)