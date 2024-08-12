# Function to encrypt the message
def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        # Shift ASCII value by key and handle wrapping around the ASCII range
        new_char = chr((ord(char) + key) % 128)
        encrypted_message += new_char
    return encrypted_message

# Function to decrypt the message
def decrypt(encrypted_message, key):
    decrypted_message = ""
    for char in encrypted_message:
        # Shift ASCII value backwards by key and handle wrapping around the ASCII range
        new_char = chr((ord(char) - key) % 128)
        decrypted_message += new_char
    return decrypted_message

# Main program to interact with the user
def main():
    # Taking user input for message, key, and mode
    message = input("Enter the message: ")
    key_input = input("Enter the key (an integer): ")
    
    # Check if the key is a valid integer
    if key_input.isdigit():
        key = int(key_input)
    else:
        print("Invalid input. The key must be an integer.")
        return  # Exit the program if the key is not valid

    # Taking mode input and stripping any extra spaces, converting to lowercase
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    
    # Validate the mode and call the appropriate function
    if mode == "encrypt":
        result = encrypt(message, key)
        print("Encrypted message:", result)
    elif mode == "decrypt":
        result = decrypt(message, key)
        print("Decrypted message:", result)
    else:
        print("Invalid mode selected. Please choose either 'encrypt' or 'decrypt'.")

# Run the program
if __name__ == "__main__":
    main()