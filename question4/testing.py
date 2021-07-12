from math import factorial

cipher = [1, 6, 24, 21, 17, 16, 25, 23, 22, 20, 19, 18, 15, 14, 13, 12, 11, 10, 9, 8, 7, 5, 4, 3, 2, 0]

factorial_number = [1, 5, 22, 19, 15, 14, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

decimal_number = 19204355291743125503999999 # 26!/21 - 1

word = 'bgyvrqzxwutsponmlkjihfedca'

def map(i):
    return chr(i + ord('a'))

def decode(cipher):
    text = ''

    for i in cipher:
        text = text + map(i)

    return text

def f(factorial_number):
    cipher = []
    n = len(factorial_number)
    S = [i for i in range(n)]
    for i in factorial_number:
        si = S[i]
        cipher.append(si)
        S.remove(si)

    return cipher

def fact_to_dec(factorial_number):
    ret = 0
    for i, v in enumerate(reversed(factorial_number)):
        ret = ret + v * factorial(i)
    return ret

print(fact_to_dec(factorial_number))
print(decode(cipher))
print(decode(f(factorial_number)))

print(decode(cipher) == word)
print(decode(cipher) == decode(f(factorial_number)))
print(f(factorial_number) == cipher)
print(fact_to_dec(factorial_number) == decimal_number)

