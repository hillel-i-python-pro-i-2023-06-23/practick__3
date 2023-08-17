from app.services.generate_keys import generate_keys
from app.services.encryption import encrypt, decrypt



def main():
    public_key, private_key = generate_keys()
    message = ''
    while True:
        print('1. Зашифровать')
        print('2. Расшифровать')
        print('3. Выход')
        choice = input('Выберите действие: ')
        if choice == '1':

            message = input("Input your message:")
            encrypted_message = encrypt(public_key, message)
            print("Encrypted message:", encrypted_message)

        elif choice == '2':
            print('1. Cвой текст')
            print('2. Тот что был зашифрован')
            choice_mod = input('Выберите действие: ')
            encrypted_message = []
            if choice_mod == '1':
                encrypted_message = input("Input encrypted_message")
            elif choice_mod == '2':
                encrypted_message = encrypt(public_key, message)

            decrypted_message = decrypt(private_key, encrypted_message)
            print("Decrypted message:", decrypted_message)

        elif choice == '3':
            break
