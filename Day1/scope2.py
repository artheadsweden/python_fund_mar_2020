def outer(x):
    def inner(y):
        return x + y
    return inner


def main():
    a = outer(100)
    print(a(10))
    b = outer(200)
    print(b(10))
    print(a(10))
    print(b(10))


if __name__ == '__main__':
    main()
