def print_pattern(n):
    # Print the pattern row by row
    for i in range(n):
        for j in range(n):
            # Calculate the value based on the pattern
            value = max(abs(i - n // 2), abs(j - n // 2)) + 1
            # Print the value followed by a space
            print(value, end=' ')
        # Move to the next line after printing each row
        print()

# Define the size of the pattern (n x n)
n = 7
print_pattern(n)

