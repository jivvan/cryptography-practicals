# # diffuse the state by interchanging columns in state matrix

# def mixColumns(state):
#     print(state)


# if __name__ == '__main__':
#     state = [42, 19, 87, 63, 56, 7, 95, 11, 34, 72, 28, 50, 9, 68, 39, 91]

#     print('Original State:', state, sep='\n')
#     mixColumns(state)
#     print('After mixColumns:', state, sep='\n')
#     # mixColumnsInverse(state)
#     # print('After mixColumnsInverse:', state, sep='\n')

# MixColumns Transformation
def mix_columns(state):
    mix_column_matrix = [
        [0x02, 0x03, 0x01, 0x01],
        [0x01, 0x02, 0x03, 0x01],
        [0x01, 0x01, 0x02, 0x03],
        [0x03, 0x01, 0x01, 0x02]
    ]

    new_state = [[0] * 4 for _ in range(4)]

    for col in range(4):
        for row in range(4):
            val = 0
            for i in range(4):
                val ^= gf_mul(mix_column_matrix[row][i], state[i][col])
            new_state[row][col] = val

    return new_state

# Inverse MixColumns Transformation


def inverse_mix_columns(state):
    inverse_mix_column_matrix = [
        [0x0e, 0x0b, 0x0d, 0x09],
        [0x09, 0x0e, 0x0b, 0x0d],
        [0x0d, 0x09, 0x0e, 0x0b],
        [0x0b, 0x0d, 0x09, 0x0e]
    ]

    new_state = [[0] * 4 for _ in range(4)]

    for col in range(4):
        for row in range(4):
            val = 0
            for i in range(4):
                val ^= gf_mul(inverse_mix_column_matrix[row][i], state[i][col])
            new_state[row][col] = val

    return new_state

# Helper function for Galois Field (GF) multiplication


def gf_mul(a, b):
    p = 0
    for _ in range(8):
        if b & 1:
            p ^= a
        high_bit_set = a & 0x80
        a <<= 1
        if high_bit_set:
            a ^= 0x1b  # Rijndael's finite field polynomial
        b >>= 1
    return p


# Example usage
state = [
    [0x32, 0x88, 0x31, 0xe0],
    [0x43, 0x5a, 0x31, 0x37],
    [0xf6, 0x30, 0x98, 0x07],
    [0xa8, 0x8d, 0xa2, 0x34]
]

print('Original State:')
for row in state:
    print(row)

mixed_state = mix_columns(state)
print("Mixed State:")
for row in mixed_state:
    print(row)

inverse_mixed_state = inverse_mix_columns(mixed_state)
print("\nInverse Mixed State:")
for row in inverse_mixed_state:
    print(row)
