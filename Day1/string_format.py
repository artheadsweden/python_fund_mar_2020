def main():
    name = "Sara"
    age = 34

    print("Hi there ", name, "! You are ", age, " years old.", sep="")
    msg1 = "Hi there {0}! You are {1} years old. Bye {0}".format(name, age)
    print(msg1)
    msg2 = f"Hi there {name}! You are {age} years old. Bye {name}"
    print(msg2)


if __name__ == '__main__':
    main()