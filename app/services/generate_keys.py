import random
import sympy

def generate_prime():  #генерит два простых числа
    while True:
        num = random.randint(0, 1000)
        if sympy.isprime(num):
            return num

def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = gcd_extended(b % a, a)
        new_x = y - (b // a) * x
        new_y = x
        return gcd, new_x, new_y

def mod_inverse(a, m):
    gcd, x, y = gcd_extended(a, m)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    else:
        return x % m

def generate_keys():
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)

    while True:
        e = random.randint(0, n)
        if sympy.gcd(e, phi) == 1:
            break

    d = mod_inverse(e, phi)

    return ((e, n), (d, n))