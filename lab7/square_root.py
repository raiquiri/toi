def root(number: int):
    x = number
    while True:
        y = (x+(number/x))/2
        if y < x:
            x = y
        else:
            return x

def main():
    number = 2359718337494319079716
    print(root(number))

if __name__ == '__main__':
    main()