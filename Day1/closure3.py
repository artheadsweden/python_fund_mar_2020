from functools import wraps


def outer(f):
    @wraps(f)
    def inner(g, n):
        return ">>> " + f(g, n) + " <<<"
    return inner


# create_greeting = outer(create_greeting)
@outer
def create_greeting(greeting, name):
    return f"{greeting}, {name}"


def main():
    msg1 = create_greeting("Hi", "Bob")
    msg2 = create_greeting("Yo", "Lisa")
    print(msg1)
    print(msg2)
    print(create_greeting.__name__)


if __name__ == '__main__':
    main()
