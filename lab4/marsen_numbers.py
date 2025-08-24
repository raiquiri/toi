# Проверяет простое ли число
def is_simple(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

def get_divisors(number):
    divisors = []
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)
    divisors.append(number)
    return sorted(divisors)

def assertion(number: int):
    if not is_simple(number) or number < 2:
        print(f'{number} is not simple')
        return False

    m_n = 2 ** number - 1
    divisors = get_divisors(m_n)

    print(f"n = {number}, M_{number} = {m_n}")
    print(f"Делители M_{number}: {divisors}")

    for divisor in divisors:
        if divisor == 1:  # пропускаем тривиальный делитель 1
            continue
        # Проверяем, имеет ли d вид 2kn + 1
        if (divisor - 1) % (2 * number) == 0:
            k = (divisor - 1) // (2 * number)
            print(f"Делитель {divisor} имеет вид 2*{k}*{number} + 1 -> Утверждение выполняется")
        else:
            print(f"Ошибка: Делитель {divisor} не имеет вида 2kn + 1!")
            return False

    print("Все делители удовлетворяют утверждению!")
    return True

def main():
    assertion(23)

if __name__ == '__main__':
    main()

