def apply_permutation(data, permutation_table):
    return ''.join(data[i-1] for i in permutation_table)


def left_shift(data, amount):
    return data[amount:]+data[:amount]


shifts = [1 if round in [1, 2, 9, 16] else 2 for round in range(1, 17)]

permuted_choice_1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    11, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

permuted_choice_2 = [
    14, 17, 11, 24,  1,  5,
    3, 28, 15,  6, 21, 10,
    23, 19, 12,  4, 26,  8,
    16,  7, 27, 20, 13,  2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]


def generate_subkeys(key):
    # convert hex key to bit string of 64 bits
    key_binary = format(int(key, 16), '064b')
    # permutate 64 bit key to 56 bits
    key_permuted = apply_permutation(key_binary, permuted_choice_1)

    # split 56 bits into two halves of 28 bits each
    C, D = key_permuted[:28], key_permuted[28:]

    subkeys = []
    for i in range(16):
        # Left shift the bits of halves
        shift_amount = shifts[i]
        C = left_shift(C, shift_amount)
        D = left_shift(D, shift_amount)
        # join halves to form 56 bits
        subkey_halves = C + D

        # compress 56 bits to 48 bit subkey
        subkey = apply_permutation(subkey_halves, permuted_choice_2)
        subkeys.append(subkey)

    return subkeys


if __name__ == '__main__':
    des_key = 'A510BB8E91F7901F'
    subkeys = generate_subkeys(des_key)

    print('Original key:', format(int(des_key, base=16), '064b'))
    print('The subkeys are:')

    for i, subkey in enumerate(subkeys):
        print(f'Subkey {i+1}: {subkey}')
