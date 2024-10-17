# odd numbers of an n term

def odd_numbers(n):
    odd_list = []
    
    for i in range(0, n+1):
        if i % 2 != 0:
            odd_list.append(i)
           
           
    print(f"The odd list is: {odd_list}")
    
        
        
odd_numbers(int(input("Enter the size of odd numbers: ")))