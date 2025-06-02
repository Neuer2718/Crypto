# Prompt the user to enter a message and store it in the variable 'message'
message = input('Enter message: ')

# Initialize an empty string to store the reversed message
translated = ''

# Start from the last character of the message
i = len(message) - 1

# Loop backwards through the message
while i >= 0:
    # Add the current character to the 'translated' string
    translated = translated + message[i]
    # Move to the previous character
    i = i - 1

# Print the reversed message
print(translated)
