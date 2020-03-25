def outer(f):
    def inner(g, n):
        return ">>> " + f(g, n) + " <<<"
    return inner


def create_greeting(greeting, name):
    return f"{greeting}, {name}"


create_greeting = outer(create_greeting)


def main():
    msg1 = create_greeting("Hi", "Bob")
    msg2 = create_greeting("Yo", "Lisa")
    print(msg1)
    print(msg2)


if __name__ == '__main__':
    main()
