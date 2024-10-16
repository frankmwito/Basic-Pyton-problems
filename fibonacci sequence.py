# Fibonacci sequence of an n term

def fibonacci_seq(n):
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_value = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_value)
    
    return fibonacci_sequence[:n]

n = int(input("Enter the size of the sequence: "))

print(fibonacci_seq(n))