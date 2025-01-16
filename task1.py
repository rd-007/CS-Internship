def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            # Perform the shift and wrap around using modulo
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabetic characters are not changed
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)  # Decrypting is just encrypting with the negative shift

def main():
    print("Caesar Cipher Program")
    while True:
        choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? (E/D): ").strip().upper()
        if choice not in ['E', 'D']:
            print("Invalid choice. Please enter 'E' for encrypt or 'D' for decrypt.")
            continue
        
        message = input("Enter your message: ")
        shift = int(input("Enter the shift value (0-25): "))
        
        if choice == 'E':
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        else:
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")
        
        another = input("Would you like to perform another operation? (Y/N): ").strip().upper()
        if another != 'Y':
            break

if __name__ == "__main__":
    main()