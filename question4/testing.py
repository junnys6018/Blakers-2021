from math import factorial

# hand calculated values 
test_decimal_number = 19204355291743125503999999 # 26!/21 - 1
test_factorial_number = [1, 5, 22, 19, 15, 14, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
test_word_in_number_form = [1, 6, 24, 21, 17, 16, 25, 23, 22, 20, 19, 18, 15, 14, 13, 12, 11, 10, 9, 8, 7, 5, 4, 3, 2, 0]
test_word = 'bgyvrqzxwutsponmlkjihfedca'

def number_to_letter(i):
    return chr(i + ord('a'))

def decode(cipher):
    text = ''

    for i in cipher:
        text = text + number_to_letter(i)

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

def dec_to_fact(decimal_number):
    factorial_number = [0]  # first digit always 0
    i = 2

    while decimal_number > 0:
        digit = decimal_number % i
        factorial_number = [digit] + factorial_number
        next_number = decimal_number // i
        #print("{} / {} = {} remainder {}".format(decimal_number, i, n, digit))
        i+=1
        decimal_number = next_number
    return factorial_number

print("Calculating f(26!/21 -1)")
decimal_number = factorial(26) // 21 - 1
print(decode(f(dec_to_fact(decimal_number))))

print("Verifying with hand calculated values")
passed = True
passed = passed and (decimal_number == test_decimal_number)
passed = passed and (dec_to_fact(decimal_number) == test_factorial_number)
passed = passed and (f(dec_to_fact(decimal_number)) == test_word_in_number_form)
passed = passed and (decode(f(dec_to_fact(decimal_number))) == test_word)

print("passed" if passed else "failed")
