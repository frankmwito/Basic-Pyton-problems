# Pyramid nested loop

def pyramid_pattern(n):
    for i in range(1, n+1):
        # Print spaces
        for j in range(n-i):
            print(" ", end="")
        # Print stars
        for k in range(2*i-1):
            print("*", end="")
        # Move to the next line
        print()

n = int(input("Enter the number of rows for the pyramid: "))
pyramid_pattern(n)
