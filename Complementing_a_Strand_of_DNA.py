# Create a string
DNA = 'AAAACCCGGT'

# Reverse the string
Reverse = DNA[::-1]

# Change the letter
Complement = Reverse.replace('A', 'X').replace('T', 'A').replace('X', 'T').replace('C', 'Y').replace('G', 'C').replace('Y', 'G')

# Print the result
print(Complement)
