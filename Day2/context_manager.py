class File:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.file_name, self.mode)
        return self.open_file

    def __exit__(self, *_):
        print("Closing")
        self.open_file.close()
        return True


def main():
    with File("MyFile2.txt", "w") as f:
        f.write("Hi there\n")
        f.write("Bye now!!!\n")



if __name__ == '__main__':
    main()
