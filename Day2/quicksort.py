def quicksort(sequence):
    return ((quicksort([x for x in sequence[1:] if x < sequence[0]]) + sequence[0:1] +
             quicksort([x for x in sequence[1:] if x >= sequence[0]])
            ) if sequence
            else [])

def main():
    values = [93, 15, 16, 78, 4, 35, 42, 6, 8, 19]
    names = ['John', 'Lisa', 'Ada', 'Bob', 'Albin']
    values = quicksort(values)
    names = quicksort(names)
    print(values)
    print(names)


if __name__ == '__main__':
    main()
