def padding(ch):
    return ord('A') if ch.isupper() else ord('a')


def encrypt(plain_text: str, key: str):
    res = ""
    while len(key) < len(plain_text):
        key += key
    for ch, k in zip(plain_text, key):
        if ch.isalpha() and k.isalpha():
            res += chr(padding(ch)+(ord(ch)+ord(k) -
                       padding(k)-padding(ch)) % 26)
        else:
            res += ch
    return res


def decrypt(cipher_text: str, key: str):
    res = ""
    while len(key) < len(cipher_text):
        key += key
    for ch, k in zip(cipher_text, key):
        if ch.isalpha() and k.isalpha():
            res += chr(padding(ch)+(ord(ch)-ord(k) +
                       padding(k)-padding(ch)) % 26)
        else:
            res += ch
    return res


if __name__ == '__main__':
    choice = 0
    while choice != 3:
        choice = int(input("1. Encrypt\t2. Decrypt\t3. Exit\n"))
        if choice == 1:
            plain_text = input("Enter plain text:")
            key = input("Enter key:")
            print(f"The encrypted cipher is: {encrypt(plain_text, key)}")
        elif choice == 2:
            cipher_text = input("Enter cipher text:")
            key = input("Enter key:")
            print(f"The plain text is: {decrypt(cipher_text, key)}")
        elif choice == 3:
            break
