def is_primitive_root(g, p):
    residues = set()
    for i in range(1, p):
        residue = pow(g, i, p)
        if residue in residues:
            return False
        residues.add(residue)
    return len(residues) == p - 1


def find_primitive_root(p):
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g


p = int(input("Enter a prime number (p): "))

primitive_root = find_primitive_root(p)

print(f"A primitive root of {p} is: {primitive_root}")
