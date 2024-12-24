4.def reverse_string_for_loop(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # Prepend character
    return reversed_str

# Example usage
print(reverse_string_for_loop("hello"))  # Output: "olleh"