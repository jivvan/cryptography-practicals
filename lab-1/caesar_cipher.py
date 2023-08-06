def encrypt(plain_text: str, key: int):
    res = ""
    for ch in plain_text:
        if ch.isalpha():
            padding = ord('A') if ch.isupper() else ord('a')
            res += chr(padding+(ord(ch)+key-padding) % 26)
        else:
            res += ch
    return res


def decrypt(cipher_text: str, key: int):
    res = ""
    for ch in cipher_text:
        if ch.isalpha():
            padding = ord('A') if ch.isupper() else ord('a')
            res += chr(padding+(ord(ch)-key-padding) % 26)
        else:
            res += ch
    return res


if __name__ == '__main__':
    choice = 0
    while choice != 3:
        choice = int(input("1. Encrypt\t2. Decrypt\t3. Exit\n"))
        if choice == 1:
            plain_text = input("Enter plain text:")
            key = int(input("Enter key:"))
            print(f"The encrypted cipher is: {encrypt(plain_text, key)}")
        elif choice == 2:
            cipher_text = input("Enter cipher text:")
            key = int(input("Enter key:"))
            print(f"The plain text is: {decrypt(cipher_text, key)}")
        elif choice == 3:
            break
