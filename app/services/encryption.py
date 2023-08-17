
def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    encrypt_text = ''.join(chr(char) for char in ciphertext)
    return encrypt_text


def decrypt(private_key, encrypt_text):
    d, n = private_key
    ciphertext = [ord(char) for char in encrypt_text]
    decrypted = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(decrypted)
