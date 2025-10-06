import struct
from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class Record:
    """Класс для представления записи с вероятностью и данными"""
    data: bytes
    access_probability: float  # Вероятность обращения p_i
    length: int = 0  # Длина данных L_i

    def __post_init__(self):
        self.length = len(self.data)

    @property
    def ratio(self) -> float:
        """Вычисляет отношение p_i / L_i"""
        return self.access_probability / self.length if self.length > 0 else 0

class Tape:
    def __init__(self, header_size: int = 4):
        self.header_size = header_size
        self.header_format = 'I'
        self.records: List[Record] = []

    # Добавить запись
    def add_record(self, data: bytes, probability: float) -> None:
        self.records.append(Record(data, probability))

    # Размещает по убыванию
    def optimize(self) -> None:
        self.records.sort(key=lambda x: x.ratio, reverse=True)

    # Создаёт ленту
    def create_tape(self) -> bytes:
        print(f'До оптимизации:\n{self.records}')
        self.optimize()
        print(f'После оптимизации:\n{self.records}')

        tape = b''
        for record in self.records:
            # Создаем заголовок с длиной данных
            header = struct.pack(self.header_format, record.length)
            # Добавляем заголовок и данные на ленту
            tape += header + record.data

        return tape

    # Поиск
    def search(self, tape: bytes, target_data: bytes) -> Optional[Tuple[int, bytes]]:
        position = 0
        tape_length = len(tape)

        while position < tape_length:
            # Читаем заголовок
            if position + self.header_size > tape_length:
                break

            header = tape[position:position + self.header_size]
            try:
                data_length = struct.unpack(self.header_format, header)[0]
            except struct.error:
                break

            # Читаем данные
            data_start = position + self.header_size
            data_end = data_start + data_length

            if data_end > tape_length:
                break

            record_data = tape[data_start:data_end]

            if record_data == target_data:
                return position, record_data

            position = data_end

        return None

def main():
    tape = Tape()

    tape.add_record(b'frequently used record', 0.4)
    tape.add_record(b"rare but long diagnostic information", 0.1)
    tape.add_record(b"help", 0.3)
    tape.add_record(b"very long error message with details", 0.05)
    tape.add_record(b"settings", 0.15)

    optimize_tape = tape.create_tape()

    messages = [b'rare but long diagnostic information', b'not existing']
    print(f'\nРезультаты поиска:\n')
    for i in range(len(messages)):
        result = tape.search(optimize_tape, messages[i])
        #print(result)

        if result:
            pos, data = result
            print(f"{i+1}. Найдено: '{data.decode()}' на позиции {pos}")
        else:
            print(f'{i+1}. Не найдено')

if __name__ == '__main__':
    main()