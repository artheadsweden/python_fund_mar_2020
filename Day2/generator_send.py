def gen_send():
    print("Starting up")
    count = 0
    while True:
        data = yield
        print(f"{count}: {data}")
        count += 1


def main():
    gs = gen_send()
    next(gs)
    print("Back in main")
    gs.send("Hi there")
    print("Back in main")
    gs.send("Bye now")


if __name__ == '__main__':
    main()
