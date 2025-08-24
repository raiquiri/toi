from typing import Dict, List, Tuple


def create_dictionary(input_str: str) -> List[Tuple[str, int]]:
    if not input_str:
        return []

    dictionary: Dict[str, int] = {}
    output: List[Tuple[str, int]] = []

    i = 0
    index = 1

    # Логи
    print(f'index\tchar\tnumber')

    while i < len(input_str):
        current_char = input_str[i]

        # Если символ уже есть в словаре
        if current_char in dictionary:
            end = i + 1
            # Поиск максимально известной последовательности
            while end <= len(input_str) and input_str[i:end] in dictionary:
                end += 1

            # Новое слово и родитель
            current_word = input_str[i:end]
            previous_word = input_str[i:end - 1]
            number_word = list(dictionary.keys()).index(previous_word) + 1

            dictionary[current_word] = number_word
            output.append((current_word, number_word))

            # Логи
            print(f'{index}\t\t{input_str[i:end]}\t\t{dictionary.get(input_str[i:end])}')

            # -1 потому что end не включается в срез и ещё -1 потому что в конце идёт инкремент
            i = end - 2

        # Если символа нет в словаре
        else:
            dictionary[current_char] = 0
            output.append((current_char, 0))

            # Логи
            print(f'{index}\t\t{current_char}\t\t0')

        i += 1
        index += 1

    return output

def char_to_binary(char: str) -> str:
    if len(char) != 1:
        raise ValueError("Только один символ")
    return bin(ord(char))[2:].zfill(8)  # 8 бит для ASCII

def number_to_binary(number: int) -> str:
    return bin(number)[2:]

def encode(input_str: str) -> str:
    dictionary = create_dictionary(input_str)
    output = ""

    for i, (char, code) in enumerate(dictionary, 1):
        if code == 0:
            output += char_to_binary(char) + " "
        else:
            output += number_to_binary(code) + " "

    return output[:-1]



def main():
    start_str = 'IF_WE_CANNOT_DO_AS_WE_WOULD_WE_SHOULD_DO_AS_WE_CAN'
    #print(f'start string:\n{start_str}')
    compress = encode(start_str)
    #print(f'compress:\n{compress}')
    print(f'total bits: {len(compress)}')


if '__main__' == __name__:
    main()