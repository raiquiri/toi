import math
import random

def ferm_test(number: int, count: int):
    if number <= 1:
        return False
    elif number == 2 or number == 3:
        return True
    if number % 2 == 0:
        return False

    # count число испытаний
    for i in range(count):
        a = random.randint(2, number - 2)

        # Логи
        print(f'{i+1}.\tnumber:{number}\tbase:{a}')

        # НОД
        if math.gcd(number, a) > 1:
            return False

        if pow(a, number - 1, number) != 1:
            return False

    return True

def main():
    number = 9703
    count = 100
    if ferm_test(number, count):
        print(f'Число {number} является составным')
    else:
        print(f'Число {number} не является составным')

if __name__ == '__main__':
    main()