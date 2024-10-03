alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.


def encrypt(original_text, shift_amount):
    encoded =''
    for letter in original_text:
        shifted_pos = alphabet.index(letter) + shift_amount    
        shifted_pos = shifted_pos % len(alphabet)   # mod functionality loop inside the list to overcome out of range error
        encoded += alphabet[shifted_pos]

    print(f'Here is the encode result: {encoded}')

encrypt(original_text='text',shift_amount=shift)   