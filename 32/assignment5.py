
5.def is_palindrome_for_loop(s):
    s = s.lower().replace(" ", "")  # Ignore spaces and case
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True

# Example usage
print(is_palindrome_for_loop("A man a plan a canal Panama"))  # Output: True
print(is_palindrome_for_loop("hello"))  # Output: False
