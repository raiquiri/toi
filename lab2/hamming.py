BITS = 25
LEVEL_LIST = []
value = 1
while value <= BITS:
    LEVEL_LIST.append(value)
    value *= 2

BITS_IN_ONE_CODE_WORD = BITS + len(LEVEL_LIST)



def bin_to_char(binary_str: str) -> str:

    if len(binary_str) != 8:
        raise ValueError("Бинарная строка должна содержать ровно 8 бит")

    if not all(bit in '01' for bit in binary_str):
        raise ValueError("Строка должна содержать только 0 и 1")

    # Преобразуем бинарную строку в число, затем в символ
    decimal_value = int(binary_str, 2)
    return chr(decimal_value)

def char_to_binary(char: str) -> str:
    if len(char) != 1:
        raise ValueError("Только один символ")
    return bin(ord(char))[2:].zfill(8)  # 8 бит для ASCII

def str_to_binary(input_str: str) -> str:
    binary_str = ""
    for char in input_str:
        binary_str += char_to_binary(char)
    return binary_str

def sum_skip(array, n):
     result = 0

     # Логи
     #print(f'array: {array}')
     #print(f'n: {n}')

     for i in range(n - 1, len(array), 2*n):
         chunk = []
         if i + n < len(array):
             chunk = array[i:i+n]
         else:
             chunk += array[i:len(array)]
         for index_item in range(len(chunk)):
             if i == n - 1 and index_item == 0:
                 continue
             result += int(chunk[index_item])
             # Логи
             #print(f'index: {i}, item: {chunk[index_item]}')

     return result

def decode(input_str: str) -> str:
    binary_list = [input_str[i:i+BITS_IN_ONE_CODE_WORD] for i in range(0, len(input_str), BITS_IN_ONE_CODE_WORD)]
    output_str = ""
    for current_word in binary_list:
        # Проверка на целостность данных
        for level in LEVEL_LIST:
            if int(current_word[level-1]) != sum_skip(current_word, level) % 2:
                return "Данные повреждены"

        # Собираем слово
        output_word = ""
        for i in range(2, len(current_word)):
            if i + 1 in LEVEL_LIST:
                continue
            else:
                output_word += current_word[i]

        output_str += bin_to_char(output_word)

    return  output_str

def encode(input_str: str) -> str:
    #binary_list = str_to_binary(input_str).split(" ")[:-1]
    binary_list = [str_to_binary(input_str)[i:i+BITS] for i in range(0, len(str_to_binary(input_str)), BITS)]
    output_str = ""
    for current_word in binary_list:
        # заполняем кодовое слово
        code_word = []
        char_index = 0
        for i in range(BITS_IN_ONE_CODE_WORD):
            if i + 1 in LEVEL_LIST:
                code_word.append(0)
            else:
                code_word.append(current_word[char_index])
                char_index += 1

        # заполняем контрольные биты
        for level in LEVEL_LIST:
            code_word[level-1] = sum_skip(code_word, level) % 2

        output_str += ''.join(str(x) for x in code_word)
        print(f'Изначальное слово: {current_word};\tЗакодированное слово: {''.join(str(x) for x in code_word)}')
    return output_str

def main():
    start_str = 'IF_WE_CANNOT_DO_AS_WE_WOULD_WE_SHOULD_DO_AS_WE_CAN'
    print(f'start_str: {start_str}')
    encode_text = encode(start_str)
    print(f'code: {encode_text}')
    decode_text = decode(encode_text)
    print(f'decode: {decode_text}')

if __name__ == '__main__':
    main()