def find_solutions(function, p):
    solutions = []
    for x in range(0, p):
        if function(x) %  p == 0:
            solutions.append(x)
    return solutions

def lift_solutions(function, function_prime, a0, p, k):
    """
    function - функция;  function_prime - производная
    а0 - найденное решение; p - просто число; k - степень модуля
    """
    if k == 1:
        return a0

    current_x = a0
    current_module = p

    for i in range(1, k):
        f_x = function(current_x)
        f_prime = function_prime(current_x)

        # Проверка, что f_x является решением
        if f_x % current_module != 0:
            print(f"Ошибка на шаге i={i}: f({current_x}) = {f_x} не делится на {current_module}.")
            return

        right_side = - (f_x // current_module) % p

        if f_prime % p == 0:
            if right_side % p != 0:
                print(f"Подъем невозможен на шаге i={i}: f'({current_x}) ≡ 0 mod {p}, но {right_side} ≠ 0 mod {p}.")
                return
            else:
                a_i = 0
                print(f"Внимание на шаге i={i}: f'({current_x}) ≡ 0 mod {p}. Выбрано a_{i} = 0.")
        else:
            try:
                # Находим обратный элемент
                inv_f_prime = pow(f_prime % p, - 1, p)
                a_i = (right_side * inv_f_prime) % p
            except ValueError:
                # Если обратный элемент не существует
                print(f"Ошибка: не удалось найти обратный элемент к f'({current_x}) = {f_prime} mod {p}.")
                return

        current_x += a_i * current_module
        current_module = current_module * p

        # Финальная проверка
    if function(current_x) % current_module == 0:
        print(f"Найдено решение: x ≡ {current_x} (mod {current_module})")
    else:
        print(f"Внимание: x = {current_x} не удовлетворяет f(x) ≡ 0 (mod {current_module}).")
        return None

    return current_x

def solve_equation(function, function_prime, p, k):
    print(f"Уравнение f(x) ≡ 0 (mod {p}^{k} = {p ** k})\n")

    # Найти a0
    solutions = find_solutions(function, p)
    if not solutions:
        print(f"Уравнение не имеет решений по модулю {p}.")
        print(f"Следовательно, нет решений и по модулю {p}^{k}.")
        return []
    print(f"Найдены решения по модулю {p}: {solutions}")

    # Подъём
    solutions_k = []
    for a0 in solutions:
        print(f"Поднимаем решение a0 = {a0}")
        solution = lift_solutions(function, function_prime, a0, p, k)
        if solution is not None:
            solutions_k.append(solution)

    return solutions_k



def main():
    function = lambda x: x**2 - 2; function_prime = lambda x: 2*x
    p = 7; k = 2
    solve_equation(function, function_prime, p, k)

if __name__ == '__main__':
    main()