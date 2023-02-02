def text_to_binary(text):
    binary = ' '.join(format(ord(i), 'b') for i in text)
    return binary

def binary_to_text(binary):
    binary_list = binary.split()
    text = ''.join(chr(int(i, 2)) for i in binary_list)
    return text

while True:
    choice = input("Enter 1 to translate text to binary and Enter 2 to translate binary to text: ")

    if choice == '1':
        text = input("Enter text or numbers: ")
        binary = text_to_binary(text)
        print("Text to Binary: " + binary)
    elif choice == '2':
        binary = input("Enter binary separated by spaces: ")
        text = binary_to_text(binary)
        print("Binary to Text: " + text)
    else:
        print("Invalid input. Please enter either 1 or 2.")

    again = input("Would you like to translate again? (yes/no): ")
    if again.lower() == 'no':
        break

print("Thank you! Goodbye")
