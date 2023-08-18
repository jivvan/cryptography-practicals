# Map 48 bits to 32 bits

lookup_table = {'0000': {'00': "0010", '01': "1110", '10': "0100", '11': "1011"},
                '0001': {'00': "1100", '01': "1011", '10': "0010", '11': "1000"},
                '0010': {'00': "0100", '01': "0010", '10': "0001", '11': "1100"},
                '0011': {'00': "0001", '01': "1100", '10': "1011", '11': "0111"},
                '0100': {'00': "0111", '01': "0100", '10': "1010", '11': "0001"},
                '0101': {'00': "1010", '01': "0111", '10': "1101", '11': "1110"},
                '0110': {'00': "1011", '01': "1101", '10': "0111", '11': "0010"},
                '0111': {'00': "0110", '01': "0001", '10': "1000", '11': "1101"},
                '1000': {'00': "1000", '01': "0101", '10': "1111", '11': "0110"},
                '1001': {'00': "0101", '01': "0000", '10': "1001", '11': "1111"},
                '1010': {'00': "0011", '01': "1111", '10': "1100", '11': "0000"},
                '1011': {'00': "1111", '01': "1010", '10': "0101", '11': "1001"},
                '1100': {'00': "1101", '01': "0011", '10': "0110", '11': "1010"},
                '1101': {'00': "0000", '01': "1001", '10': "0011", '11': "0100"},
                '1110': {'00': "1110", '01': "1000", '10': "0000", '11': "0101"},
                '1111': {'00': "1001", '01': "0110", '10': "1110", '11': "0011"}
                }


def mapping(section: str):
    outer_bits = section[0]+section[-1]
    inner_bits = section[1:-1]
    return lookup_table[inner_bits][outer_bits]


def convert_to_bit_string(key: int):
    bit_string = bin(key).split('b')[1]
    if len(bit_string) < 48:
        bit_string = '0'*(48-len(bit_string))+bit_string
    return bit_string


def convert_to_decimal(key: str): return int('0b'+key, base=2)


def s_box(key: int):
    bit_key = convert_to_bit_string(key)
    if len(bit_key) != 48:
        raise Exception("input key should be 48 bits")
    sections = [bit_key[i:i+6] for i in range(0, 48, 6)]
    res = [mapping(section) for section in sections]
    return "".join(res)


if __name__ == '__main__':
    key = int(input('Enter key as decimal:'))
    shrinked_key = s_box(key)
    print(
        f"The 32 bit key is: {shrinked_key}, decimal: {convert_to_decimal(shrinked_key)}")
