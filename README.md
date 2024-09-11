# File-Encryptor

File Encryption and Decryption Script

This Python script demonstrates a simple file encryption and decryption process. It creates a sample file, generates a random encryption key, encrypts the file’s content, and then decrypts it back to the original message.

Features
File Creation: Creates a file named original_message.txt with a sample message.
Random Encryption Key: Generates a random encryption key for letters, numbers, and symbols.
Message Encryption: Encrypts the content of the sample file using the generated key.
Message Decryption: Decrypts the encrypted message back to its original form.
File Handling: Reads from and writes to text files to store the original, encrypted, and decrypted messages.

Code Overview
create_sample_file(): Creates a sample file with a message.
generate_encryption_key(): Generates a random encryption key.
encrypt_message(message, encryption_key): Encrypts a given message using the encryption key.
decrypt_message(encrypted_message, encryption_key): Decrypts an encrypted message using the encryption key.
main(): Orchestrates the file creation, encryption, and decryption processes
