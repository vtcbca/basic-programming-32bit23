
3.def fibonacci_while_loop(max_value):
    fib_sequence = []
    a, b = 0, 1
    while a <= max_value:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Example usage
print(fibonacci_while_loop(50))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]