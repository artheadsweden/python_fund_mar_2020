from contextlib import contextmanager

@contextmanager
def open_file(file_name, mode):
    # This is the enter part
    print("Starting context manager")
    the_file = open(file_name, mode)
    yield the_file

    # This is the exit part
    print("Closing file")
    the_file.close()


def main():
    with open_file("MyFile3.txt", "w") as f:
        print("Entering context manager")
        f.write("Hi there\n")
        f.write("Bye there\n")
        print("Exiting context manager")


if __name__ == '__main__':
    main()
