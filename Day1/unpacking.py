def func():
    a = 10
    b = 20
    c = 30
    return a, b, c


def main():
    x, y, z = func()
    r = func()

    print(x, y, z)
    print(r)

    numbers = (1, 2, 3, 4, 5, 6)
    one, two, three, four, five, six = numbers
    first, *rest, second_last,  last = numbers
    print(first)
    print(rest)
    print(second_last)
    print(last)

    first, *_, last = numbers


if __name__ == '__main__':
    main()