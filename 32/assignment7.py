7.def triangle_while_loop(n):
    i = 1
    while i <= n:
        print(' ' * (n - i) + ' '.join(str(x) for x in range(1, 2 * i)))
        i += 1

# Example usage
triangle_while_loop(3)