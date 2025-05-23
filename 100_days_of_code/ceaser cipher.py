import ceaser_cipher_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(ceaser_cipher_art.logo)



# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.

# TODO-1: Import and print the logo from art.py when the program starts.
# TODO-2: What happens if the user enters a number/symbol/space?
# TODO-3: Can you figure out a way to restart the cipher program?

def caeser(original_text,shift_amount, encode_decode):
    output_text =''
    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else: 
            if encode_decode == 'encode':
                shifted_pos = alphabet.index(letter) + shift_amount  
            elif encode_decode == 'decode':
                shifted_pos = alphabet.index(letter) - shift_amount
            shifted_pos = shifted_pos % len(alphabet)   # mod functionality loop inside the list to overcome out of range error
            output_text += alphabet[shifted_pos]

    print(f'Here is the {encode_decode}d result: {output_text}') 

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caeser(original_text=text,shift_amount=shift,encode_decode=direction)

    cont = input("Type 'yes' if you want to go again. Otherwise, type 'no'.").lower()
    if cont == 'no':
        should_continue = False
        print("Goodbye!")