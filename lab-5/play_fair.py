from collections import namedtuple


Index = namedtuple('Index', 'i j')


def generate_table(key: str):
    key = "".join(dict.fromkeys(key+'abcdefghiklmnopqrstuvwxyz'))
    res = []
    rows = []
    for key_el in key:
        rows.append(key_el)
        if len(rows) == 5:
            res.append(rows.copy())
            rows.clear()
    return res


def print_table(table):
    print('The playfair table is:')
    # Print the table header
    print('+' + '-'*12 + '+' + '-'*12 + '+' + '-' *
          12 + '+' + '-'*12 + '+' + '-'*12 + '+')

    # Print table rows with separators
    for i, row in enumerate(table):
        for cell in row:
            print(f'| {cell:<10} ', end='')
        print('|')  # End the row with a vertical bar

        # Add a separator after each row (except the last one)
        print('+' + '-'*12 + '+' + '-'*12 + '+' + '-' *
              12 + '+' + '-'*12 + '+' + '-'*12 + '+')


def get_table_index(table: list, chars: tuple) -> list[Index]:
    res = []
    for char in chars:
        for i, row in enumerate(table):
            for j, col in enumerate(row):
                if char == col:
                    res.append(Index(i, j))
    return res


# iterate over items two at a time
def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)


def preprocess_args(text: str, key: str):
    # convert plain text and key to lower text and replace j's in them with i's
    # since j's and i's are conjoined in algorithm
    text = text.lower().replace('j', 'i')
    key = key.lower().replace('j', 'i')

    # generate the playfair table and print it
    table = generate_table(key)
    print_table(table)

    # if odd no of chars in plain text, make it even
    # since chars are encrypted pariwise
    if len(text) % 2 != 0:
        text += 'z'
    return text, table


def encrypt(plain_text: str, key: str):
    # generate table and normalize plain text
    plain_text, table = preprocess_args(plain_text, key)
    res = ""
    for chars in pairwise(plain_text):
        ind1, ind2 = get_table_index(table, chars)
        # if same row, next elements in row, i.e. one circular right character
        if ind1.i == ind2.i:
            res += table[ind1.i][(ind1.j+1) % 5]
            res += table[ind2.i][(ind2.j+1) % 5]
        # if same column, next element in column, i.e. one circular down character
        elif ind1.j == ind2.j:
            res += table[(ind1.i+1) % 5][ind1.j]
            res += table[(ind2.i+1) % 5][ind2.j]
        else:
            res += table[ind1.i][ind2.j]
            res += table[ind2.i][ind1.j]
    return res


def decrypt(cipher_text: str, key: str):
    # generate table and normalize cipher text
    cipher_text, table = preprocess_args(cipher_text, key)

    res = ""
    for chars in pairwise(cipher_text):
        ind1, ind2 = get_table_index(table, chars)
        # if same row, previous elements in row, i.e. one circular left character
        if ind1.i == ind2.i:
            res += table[ind1.i][(ind1.j-1) % 5]
            res += table[ind2.i][(ind2.j-1) % 5]
        # if same column, previous element in column, i.e. one circular up character
        elif ind1.j == ind2.j:
            res += table[(ind1.i-1) % 5][ind1.j]
            res += table[(ind2.i-1) % 5][ind2.j]
        else:
            res += table[ind1.i][ind2.j]
            res += table[ind2.i][ind1.j]
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
