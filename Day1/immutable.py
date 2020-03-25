def main():
    # x ---------------> 11
    #        |--> 10
    # y -----
    x = 10
    y = 10
    print(id(x))
    print(id(y))
    x += 1
    print(id(x))
    print(id(y))

    print("-"*30)
    name1 = "Peter"
    name2 = "Peter"
    print(id(name1))
    print(id(name2))



if __name__ == '__main__':
    main()