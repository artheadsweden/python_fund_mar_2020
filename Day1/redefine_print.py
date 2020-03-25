from functools import wraps


def redefined_print(original_print):
    @wraps(original_print)
    def wrapper(*args, **kwargs):
        pre = kwargs.get("start", "")
        if "start" in kwargs:
            kwargs.pop("start")
        original_print(pre, *args, **kwargs)
    return wrapper


print = redefined_print(print)


def main():
    name = "Sue"
    age = 34
    print("This is", name, "who is", age, "years old", sep=" ")
    print("This works", start="---> ")
    print(print.__name__)


if __name__ == '__main__':
    main()
