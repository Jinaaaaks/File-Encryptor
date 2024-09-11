import os
import random

def create_sample_file():
    # Create a file named 'original_message.txt' and write a sample message into it
    with open('original_message.txt', 'w') as file:
        file.write("Hello, World!")

def generate_encryption_key():
    """Generate a random encryption key for letters, numbers, and symbols."""
    # Define possible characters: uppercase letters, lowercase letters, numbers, and symbols
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    symbols = '!@#$%^&*()_+-=[]{}|;:\'",.<>?/£~'
    characters = alphabet_upper + alphabet_lower + numbers + symbols

    # Generate a list of random numbers to be used as the encryption key
    random_numbers = random.sample(range(10000, 10000 + len(characters)), len(characters))

    # Create a dictionary that maps each character to a unique random number
    encryption_key = {char: num for char, num in zip(characters, random_numbers)}

    return encryption_key

def encrypt_message(message, encryption_key):
    # Encrypt the given message using the provided encryption key
    encrypted_message = []
    for char in message:
        if char in encryption_key:
            encrypted_message.append(str(encryption_key[char]))  # Replace character with its encrypted value
        else:
            encrypted_message.append(char)  # Keep the character unchanged if it's not in the key
    return ' '.join(encrypted_message)  # Join encrypted values with spaces

def decrypt_message(encrypted_message, encryption_key):
    # Decrypt the encrypted message using the provided encryption key
    decryption_key = {str(value): key for key, value in encryption_key.items()}  # Reverse the encryption key

    decrypted_message = []
    for num in encrypted_message.split():
        if num in decryption_key:
            decrypted_message.append(decryption_key[num])  # Replace encrypted value with the original character
        else:
            decrypted_message.append(num)  # Keep the value unchanged if it's not in the key
    return ''.join(decrypted_message)  # Join the decrypted characters

def main():
    # Print the current working directory
    print("Current Working Directory:", os.getcwd())

    create_sample_file()  # Create the file 'original_message.txt' with a sample message

    encryption_key = generate_encryption_key()  # Generate a random encryption key

    with open('original_message.txt', 'r') as file:
        original_message = file.read()  # Read the original message from the file

    encrypted_message = encrypt_message(original_message, encryption_key)  # Encrypt the original message

    with open('encrypted_message.txt', 'w') as file:
        file.write(encrypted_message)  # Write the encrypted message to 'encrypted_message.txt'

    with open('encrypted_message.txt', 'r') as file:
        encrypted_message_read = file.read()  # Read the encrypted message from the file

    decrypted_message = decrypt_message(encrypted_message_read, encryption_key)  # Decrypt the message

    with open('decrypted_message.txt', 'w') as file:
        file.write(decrypted_message)  # Write the decrypted message to 'decrypted_message.txt'

    # Inform the user that the encryption and decryption process is complete
    print("Encryption and Decryption process completed.")
    print("Check 'encrypted_message.txt' and 'decrypted_message.txt' for the results.")

if __name__ == '__main__':
    main()
