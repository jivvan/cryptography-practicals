def matrix_mul(mat1, mat2):
    result = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            result[i] += mat1[i][j] * mat2[j]
        result[i] %= 26
    return result


def main():
    a = [
        [6, 24, 1],
        [13, 16, 10],
        [20, 17, 15]
    ]

    b = [
        [8, 5, 10],
        [21, 8, 21],
        [21, 12, 8]
    ]

    msg = input("Enter plain text: ")
    c = []

    for i in range(3):
        c.append(ord(msg[i]) - 65)
        print(c[i], end=" ")

    d = matrix_mul(a, c)

    print("\nEncrypted Cipher Text:", end=" ")
    for i in range(3):
        print(chr(d[i] + 65), end=" ")

    c = matrix_mul(b, d)

    print("\nDecrypted Cipher Text:", end=" ")
    for i in range(3):
        print(chr(c[i] + 65), end=" ")


if __name__ == "__main__":
    main()
