from key_gen import generate_subkeys
from s_box import shrink_key

# Initial Permutation (IP) table
initial_permutation_table = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# Inverse Permutation (IP-1) table
inverse_permutation_table = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9,  49, 17, 57, 25
]

# Expansion permutation table
expansion_table = [
    32,  1,  2,  3,  4,  5,
    4,  5,  6,  7,  8,  9,
    8,  9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32,  1
]

# P-box permutation table
pbox_table = [
    16,  7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2,  8, 24, 14,
    32, 27,  3,  9,
    19, 13, 30,  6,
    22, 11,  4, 25
]


def initial_permutation(input_str):
    # Check if the input string is exactly 64 bits
    if len(input_str) != 64:
        raise ValueError("Input string must be 64 bits long.")

    # Apply the initial permutation
    permuted_str = ''.join(input_str[i - 1] for i in initial_permutation_table)

    return permuted_str


def inverse_permutation(permuted_str):
    # Check if the input string is exactly 64 bits
    if len(permuted_str) != 64:
        raise ValueError("Input string must be 64 bits long.")

    # Apply the inverse permutation
    original_str = ''.join(permuted_str[i - 1]
                           for i in inverse_permutation_table)

    return original_str


def expand_right_half(right_half):
    # Perform expansion
    expanded_half = [right_half[bit - 1] for bit in expansion_table]

    # Convert the expanded list back to a string
    expanded_half_str = ''.join(expanded_half)

    return expanded_half_str


def pbox_permutation(sbox_output):
    # Perform permutation
    permuted_output = [sbox_output[bit - 1] for bit in pbox_table]

    # Convert the permuted list back to a string
    permuted_output_str = ''.join(permuted_output)

    return permuted_output_str


def encrypt(plain_text, key):
    # Initial Permutation
    plain_text = initial_permutation(
        format(int(plain_text, 16), '064b'))

    # Key generation
    subkeys = generate_subkeys(key)

    # 16 rounds of encryption
    for i in range(16):
        # Round key for this round
        round_key = subkeys[i]

        # Divide plain text into two 32 bit halves
        left_half, right_half = plain_text[:32], plain_text[32:]

        # Expand right half to 48 bits for F(R, K)
        expanded_right_half = expand_right_half(right_half)

        # X-OR 48 bit right half with the 48 bit round key
        round_key_xor_res = int(expanded_right_half, 2) ^ int(round_key, 2)
        round_key_xor_res = format(round_key_xor_res, '048b')

        # Apply S-Box to convert 48 bit text to 32 bits
        shriked_res = shrink_key(round_key_xor_res)

        # Apply permutation to 32 bit output from s-box output
        permuted_res = pbox_permutation(shriked_res)

        left_half_xor_res = int(permuted_res, 2) ^ int(left_half, 2)
        left_half_xor_res = format(left_half_xor_res, '032b')
        plain_text = right_half + left_half_xor_res

    cipher_text = inverse_permutation(plain_text)
    return hex(int(cipher_text, 2))


if __name__ == '__main__':
    res = encrypt('7265636472656364', '133457799bbcdff1')
    print(res)

    print(hex(int('1100101011101001001001101000001110101101010001001001001101000001', 2)))
