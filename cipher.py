def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
        else:
            shifted_char = char
        result += shifted_char
    return result

while True:
    mode = input("Choose 'encrypt' or 'decrypt': ").lower()
    if mode in ("encrypt", "decrypt"):
        break
    else:
        print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")

text = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

# Apply the shift in the correct direction based on the mode
if mode == "encrypt":
    encrypted_text = caesar_cipher(text, shift)
    print("Encrypted text:", encrypted_text)
elif mode == "decrypt":
    decrypted_text = caesar_cipher(text, -shift)
    print("Decrypted text:", decrypted_text)