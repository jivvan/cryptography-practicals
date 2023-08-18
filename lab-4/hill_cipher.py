import numpy as np
import math


def ascii_to_number(ch): return ord(
    ch) - (ord('a') if ch.lower() else ord('A'))


def number_to_ascii(num): return chr(ord('a') + num)


np_number_to_ascii = np.vectorize(number_to_ascii)
np_mod = np.vectorize(lambda x: x % 26)


def generate_key_matrix(key):
    n = len(key)
    while math.sqrt(n) != math.floor(math.sqrt(n)):
        n += 1
    mat_size = int(math.sqrt(n))
    key_list = list(key)
    key_list.extend(['Z' for _ in range(n-len(key))])
    res = [[] for _ in range(mat_size)]
    for i, _ in enumerate(res):
        for _ in range(mat_size):
            res[i].append(ascii_to_number(key_list.pop(0)))
    return np.array(res)


def generate_plain_text_matrix(plain_text: str, matrix_width):
    plain_text_list = list(plain_text)
    res = []
    while plain_text_list:
        temp = []
        for _ in range(matrix_width):
            temp.append(ascii_to_number(plain_text_list.pop(0) if len(
                plain_text_list) > 0 else 'z'))
        res.append(temp)
    return np.matrix.transpose(np.array(res))


plain_text = input("Enter plain text:")
key = input("Enter key:")

key_matrix = generate_key_matrix(key)
plain_text_matrix = generate_plain_text_matrix(plain_text, len(key_matrix))
print(key_matrix, plain_text_matrix)
resultant_matrix = np.dot(key_matrix, plain_text_matrix)
resultant_matrix = np.matrix.transpose(resultant_matrix)
resultant_matrix = np_mod(resultant_matrix)
resultant_matrix = np_number_to_ascii(resultant_matrix)

print(resultant_matrix)
