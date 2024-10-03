alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.



def ceaser(original_text,shift_amount, encode_decode):
    output_text =''
    for letter in original_text:
        if encode_decode == 'encode':
            shifted_pos = alphabet.index(letter) + shift_amount  
        elif encode_decode == 'decode':
            shifted_pos = alphabet.index(letter) - shift_amount
        shifted_pos = shifted_pos % len(alphabet)   # mod functionality loop inside the list to overcome out of range error
        output_text += alphabet[shifted_pos]

    print(f'Here is the {encode_decode}d result: {output_text}')
    pass

ceaser(original_text=text,shift_amount=shift,encode_decode=direction)