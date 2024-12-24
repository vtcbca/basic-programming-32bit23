solution


1.def factorial_while_loop(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

# Example usage
print(factorial_while_loop(5))  # Output: 120


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



3.def fibonacci_while_loop(max_value):
    fib_sequence = []
    a, b = 0, 1
    while a <= max_value:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Example usage
print(fibonacci_while_loop(50))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]



4.def reverse_string_for_loop(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # Prepend character
    return reversed_str

# Example usage
print(reverse_string_for_loop("hello"))  # Output: "olleh"


5.def is_palindrome_for_loop(s):
    s = s.lower().replace(" ", "")  # Ignore spaces and case
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True

# Example usage
print(is_palindrome_for_loop("A man a plan a canal Panama"))  # Output: True
print(is_palindrome_for_loop("hello"))  # Output: False


6.def pattern_while_loop(n):
    i = 1
    while i <= n:
        print('* ' * i)
        i += 1

# Example usage
pattern_while_loop(4)


7.def triangle_while_loop(n):
    i = 1
    while i <= n:
        print(' ' * (n - i) + ' '.join(str(x) for x in range(1, 2 * i)))
        i += 1

# Example usage
triangle_while_loop(3)


8.def alphabet_pattern_while_loop(n):
    i = 1
    while i <= n:
        # Calculate spaces for the current row
        spaces = ' ' * (n - i) * 2
        
        # Create the alphabet sequence
        forward_seq = [chr(65 + j) for j in range(i)]  # A, B, C, ...
        backward_seq = forward_seq[:-1][::-1]  # A, B, ... and then reversed
        
        # Combine forward and backward sequence
        row = forward_seq + backward_seq
        
        # Print the row with spaces
        print(spaces + '   '.join(row))
        i += 1

# Example usage
alphabet_pattern_while_loop(3)
