# https://en.wikipedia.org/wiki/Rail_fence_cipher

def find_fence_ind(i, rails, down):
    return i % (rails-1) if down else (rails-1) - (i % (rails-1))


def find_stuff(str_len: int, rails: int):
    diagonals = 1
    while rails + ((rails-1)*diagonals) < str_len:
        diagonals += 1
    blanks = (rails + ((rails-1)*diagonals)) - str_len
    return blanks


def len_of_longest_subarray(arr: list):
    return len(sorted(arr, key=lambda x: len(x), reverse=True)[0])


def encrypt(plain_text: str, rails: int):
    if rails <= 1:
        return plain_text
    fences = [""]*rails
    down = False
    for i, ch in enumerate(plain_text):
        if i % (rails-1) == 0:
            down = not down
        fence_ind = find_fence_ind(i, rails, down)
        fences[fence_ind] += ch
    return "".join(fences)


def decrypt(cipher_text: str, rails: int):
    if rails <= 1:
        return cipher_text
    blanks = find_stuff(len(cipher_text)-1, rails)
    res = [[] for _ in range(rails)]
    down = False
    for i in range(len(cipher_text)+blanks):
        if i >= len(cipher_text):
            res[find_fence_ind(i, rails, down)].append(None)
        else:
            if i % (rails-1) == 0:
                down = not down
            longest_len = len_of_longest_subarray(res)
            fence_ind = find_fence_ind(i, rails, down)
            while len(res[fence_ind]) != longest_len:
                res[fence_ind].append(None)
            res[fence_ind].append("")
    list_of_chrs = list(cipher_text)
    for i, row in enumerate(res):
        for j, ch in enumerate(row):
            if ch is not None:
                res[i][j] += list_of_chrs.pop(0)
    plain_text = ""
    for j in range(len_of_longest_subarray(res)):
        for i, row in enumerate(res):
            if j < len(row) and row[j] is not None:
                plain_text += row[j]
    return plain_text


if __name__ == '__main__':
    choice = 0
    while choice != 3:
        choice = int(input("1. Encrypt\t2. Decrypt\t3. Exit\n"))
        if choice == 1:
            plain_text = input("Enter plain text:")
            rails = int(input('Enter no of rails:'))
            print(f"The encrypted cipher is: {encrypt(plain_text, rails)}")
        elif choice == 2:
            cipher_text = input("Enter cipher text:")
            rails = int(input('Enter no of rails:'))
            print(f"The plain text is: {decrypt(cipher_text, rails)}")
        elif choice == 3:
            break
