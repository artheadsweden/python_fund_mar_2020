from mymodule.calc import add
from mymodule import MY_CONSTANT
#import mymodule.calc as calc


def main():
    print(MY_CONSTANT)
    print(add(3, 4))
    #print(calc.add(6, 9))


if __name__ == '__main__':
    main()
