
def list_adder(name, the_list=[]):
    the_list.append(name)
    return the_list


def list_adder2(name, the_list=None):
    if the_list is None:
        the_list = []
    the_list.append(name)
    return the_list


def main():
    names = list_adder2("Peter")
    print(names)
    names = list_adder2("Anna")
    print(names)

if __name__ == '__main__':
    main()