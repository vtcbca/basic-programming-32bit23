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
