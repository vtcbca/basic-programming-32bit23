
2.def is_prime_while_loop(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# Example usage
print(is_prime_while_loop(11))  # Output: True
print(is_prime_while_loop(15))  # Output: False
