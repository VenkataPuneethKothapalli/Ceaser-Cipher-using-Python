# Caesar Cipher Encryption Program (Python)

def encrypt(text, shift):
    result = ""

    for character in text:
        # Check if the character is a letter
        if character.isalpha():
            # Decide base ASCII value based on case
            if character.islower():
                base = ord('a')
            else:
                base = ord('A')

            # Caesar Cipher formula
            shifted_char = (ord(character) - base + shift) % 26 + base

            # Convert ASCII to character and add to result
            result += chr(shifted_char)
        else:
            # Non-letter characters remain unchanged
            result += character

    return result


# ---------------- MAIN PROGRAM ----------------
print("🔐 Caesar Cipher Encryption Program")

text = input("Enter text to encrypt: ")
shift = int(input("Enter shift key (0-25): "))

encrypted_text = encrypt(text, shift)

print("Encrypted text:", encrypted_text)
