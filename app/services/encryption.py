
def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext


def decrypt(private_key, ciphertext):
    d, n = private_key
    decrypted = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(decrypted)
