import os

def caesar_encrypt(text, shift):
    result = ""
    shift = shift % 26 
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    result = ""
    shift = shift % 26 
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset - shift + 26) % 26 + ascii_offset)
        else:
            result += char
    return result

def process_file(file_name, shift, operation):
    try:
        if operation == 'encrypt':
            if not os.path.exists(file_name):
                create_new = input(f"The file '{file_name}' does not exist. Do you want to create it? (yes/no): ").strip().lower()
                if create_new == 'yes':
                    content = input("Enter the content to save in the new file: ")
                    with open(file_name, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"File '{file_name}' created successfully.")
                else:
                    print("File creation aborted.")
                    return

            with open(file_name, "r", encoding="utf-8") as f:
                text = f.read()
            processed_text = caesar_encrypt(text, shift)
            new_file_name = file_name + ".encrypted"

        elif operation == 'decrypt':
            encrypted_file = file_name + ".encrypted"
            if not os.path.exists(encrypted_file):
                print(f"The encrypted file '{encrypted_file}' does not exist.")
                return

            with open(encrypted_file, "r", encoding="utf-8") as f:
                text = f.read()
            processed_text = caesar_decrypt(text, shift)
            new_file_name = file_name + ".decrypted"
        else:
            print("Invalid operation. Use 'encrypt' or 'decrypt'.")
            return

        with open(new_file_name, "w", encoding="utf-8") as f:
            f.write(processed_text)
        print(f"File {operation}ed successfully: {new_file_name}")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        print("\nBasic Encryption Program")
        print("1. Encrypt file")
        print("2. Decrypt file")
        print("3. Quit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            file_name = input("Enter file name to encrypt: ")
            try:
                shift = int(input("Enter shift value: "))
                process_file(file_name, shift, 'encrypt')
            except ValueError:
                print("Invalid shift value. Please enter a valid integer.")

        elif choice == "2":
            file_name = input("Enter file name to decrypt: ")
            try:
                shift = int(input("Enter shift value: "))
                process_file(file_name, shift, 'decrypt')
            except ValueError:
                print("Invalid shift value.")
                
        elif choice == "3":
            print("Quit")
            break
            
        else:
            print("Invalid Option.")

main()
