x = 10


def main():
    #global x
    x = 1
    print(x)
    #x += 1

    def inner():
        nonlocal x
        x += 1
        print(x)  # LEGB

    inner()


if __name__ == '__main__':
    main()
