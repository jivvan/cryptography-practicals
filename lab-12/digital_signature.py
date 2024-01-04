import random
import hashlib


def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1

    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


p = int(input("Enter prime modulo p: "))
q = int(input("Enter prime divisor q: "))
message = input("Enter the message to sign: ")
x = random.randint(1, q - 1)

g = 2
y = pow(g, x, p)

k = int(
    input("Enter a random number k: ")
)  # Random number (in practice, this should be generated randomly)
r = pow(g, k, p) % q
h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
k_inverse = mod_inverse(k, q)
s = (k_inverse * (h + x * r)) % q

# Verifying the signature
w = mod_inverse(s, q)
u1 = (h * w) % q
u2 = (r * w) % q
v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q

is_valid = v == r

print(f"\nOriginal Message: {message}")
print(f"Public Key [p, q, g, y]: [{p}, {q}, {g}, {y}]")
print(f"Private Key [p, q, g, x]: [{p}, {q}, {g}, {x}]")
print(f"Signature (r, s): ({r}, {s})")

# Verification step
if is_valid:
    print("Signature is verified.")
else:
    print("Signature verification failed.")
