# The encrypted message
message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'

# The set of possible symbols used in the message
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?.'

# Loop through every possible key
for key in range(len(SYMBOLS)):
    # Start with a blank string to store the translated message
    translated = ''

    # Loop through each symbol in the message
    for symbol in message:
        # If the symbol is in the SYMBOLS set, decrypt it
        if symbol in SYMBOLS:
            # Find the index of the symbol in SYMBOLS
            symbolIndex = SYMBOLS.find(symbol)

            # Decrypt the symbol by subtracting the key
            translatedIndex = symbolIndex - key

            # Handle wrap-around if needed
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            # Add the decrypted symbol to the translated message
            translated = translated + SYMBOLS[translatedIndex]
        else:
            # If the symbol is not in SYMBOLS, leave it unchanged
            translated = translated + symbol

    # Display the key number and its corresponding decrypted message
    print('Key #%s: %s' % (key, translated))