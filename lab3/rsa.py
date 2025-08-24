from typing import List

def numbers_to_string(ascii_codes):
    return ''.join(chr(code) for code in ascii_codes)

def string_to_numbers(text):
    return [ord(char) for char in text]

# Расширенный алгоритм Эвклида
def gcde(a: int, b: int):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcde(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y

def create_private_key(e:int, f: int) -> int:
    d = gcde(e, f)[1]
    if d >= 0:
        return d
    return d + f

def decode(message: List[int], private_key) -> List[int]:
    code: List[int] = []
    for char in message:
        code.append((char ** private_key[1]) % private_key[0])
    return code

def encode(message: List[int], public_key) -> List[int]:
    code: List[int] = []
    for char in message:
        code.append((char ** public_key[1]) % public_key[0])
    return code

def main():
    message = 'IF_WE_CANNOT_DO_AS_WE_WOULD_WE_SHOULD_DO_AS_WE_CAN'
    int_message = string_to_numbers(message)

    p = 269; q = 271; e = 65537
    n = p * q; f = (p - 1) * (q - 1)

    public_key = [n, e]
    private_key = [n, create_private_key(e, f)]

    code_message = encode(int_message, public_key)
    decode_message = decode(code_message, private_key)

    print(f'start message: {message}')
    print(f'code message: {code_message}')
    print(f'decode message: {numbers_to_string(decode_message)}')

if __name__ == '__main__':
    main()