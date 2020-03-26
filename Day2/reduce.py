from functools import reduce

def func(a, b):
    return a + b


def largest(a, b):
    return a if a > b else b


def main():
    numbers = [34, 1, 23, 89, 2, 7, 98, 5]
    result = reduce(func, numbers)
    print(result)
    print(sum(numbers))

    result = reduce(largest, numbers)
    print(result)

    result = reduce(lambda a, b: a if a < b else b, numbers)
    print(result)

    min, *_, max = sorted(numbers)
    print(min, max)

if __name__ == '__main__':
    main()
