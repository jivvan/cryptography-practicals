import math
import random


def is_prime(n, k=5):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False

    # Write n as 2^r * d + 1
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def get_random_prime(n: int):
    while True:
        probable_prime = random.getrandbits(n)
        if is_prime(probable_prime):
            return probable_prime


def mod_inverse(a, m):
    m0 = m
    x0, x1 = 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1


def generate_keys(p, q):
    n = p * q
    phi = (p-1) * (q-1)

    e = random.randrange(1, phi)
    while math.gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    d = mod_inverse(e, phi)

    return ((e, n), (d, n))


def encrypt(message, public_key):
    e, n = public_key
    enc_msg = [pow(ord(char), e, n) for char in message]
    return enc_msg


def decrypt(enc_msg, private_key):
    d, n = private_key
    msg = [pow(char, d, n) for char in enc_msg]
    return "".join([chr(code) for code in msg])


if __name__ == '__main__':
    p = get_random_prime(32)
    q = get_random_prime(32)

    print('p:', p, ', q:', q)

    public_key, private_key = generate_keys(p, q)

    message = "We are discovered, run for your life!"
    print('Message', message)

    cipher_text = encrypt(message, public_key)
    print('Cipher text:', "".join([chr(code % 128) for code in cipher_text]))

    plain_text = decrypt(cipher_text, private_key)
    print('Plain text:', plain_text)
