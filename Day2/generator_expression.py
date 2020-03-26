def main():
    numbers = [1, 2, 3, 4, 5, 6]
    result = (value*2 for value in numbers)
    print(list(result))
    print(list(result))


if __name__ == '__main__':
    main()
