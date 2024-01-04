def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def are_relatively_prime(num1, num2):
    return gcd(num1, num2) == 1


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if are_relatively_prime(num1, num2):
    print(f"{num1} and {num2} are relatively prime.")
else:
    print(f"{num1} and {num2} are not relatively prime.")
