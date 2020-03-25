def fun_fact(e):
    def inner(b):
        return b**e
    return inner


def main():
    square = fun_fact(2)
    cube = fun_fact(3)
    print(square(3))
    print(square(4))
    print(cube(3))
    print(cube(4))

    funcs = [fun_fact(i) for i in range(2, 100)]
    for func in funcs:
        print(func(2))


if __name__ == '__main__':
    main()
