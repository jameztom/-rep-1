original_string = input("Enter string:")
reversed_string = ""

# Iterate through the characters of the original string in reverse order
for char in original_string[::-1]:
    reversed_string += char

print("Original String:", original_string)
print("Reversed String:", reversed_string)
