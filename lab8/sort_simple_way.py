def sort(array: list[int]) -> list[int]:
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        if array[min_index] < array[i]:
            temp = array[i]
            array[i] = array[min_index]
            array[min_index] = temp

    return array

def main():
    num_array = [64, 25, 12, 3, 22, 11]
    print(sort(num_array))

if __name__ == '__main__':
    main()