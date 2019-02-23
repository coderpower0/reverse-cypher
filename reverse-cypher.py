from string import ascii_letters

cipher_letters = 'zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA'


def cipher(text):
    trans = str.maketrans(ascii_letters, cipher_letters)
    return text.translate(trans)

def decipher(text):
    trans = str.maketrans(cipher_letters, ascii_letters)
    return text.translate(trans)

if __name__ == '__main__':

    text_to_cipher = input("please enter the text you want to cypher: ")
    ciphered = cipher(text_to_cipher)
    print(f"Cipheres text: {ciphered}")