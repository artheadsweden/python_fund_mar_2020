def my_gen(n):
    print("Starting")
    i = 0
    while i < n:
        yield i
        i += 1


def seq_generate(n):
    seq = []
    i = 0
    while i < n:
        seq.append(i)
        i += 1
    return seq


def main():
    g = my_gen(3)
    print(next(g))
    print(next(g))

    print("Entering the for-loop")
    for i in g:
        print(i)

    for value in my_gen(10):
        print(value)


if __name__ == '__main__':
    main()
