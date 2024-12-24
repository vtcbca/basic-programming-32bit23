1.def factorial_while_loop(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

# Example usage
print(factorial_while_loop(5))  # Output: 120