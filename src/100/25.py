#! python3

from fib import fib

def main():
    i = 1
    while True:
        n = fib(i)

        if len(str(n)) == 1000:
            return i

        i += 1

if __name__ == '__main__':
    print(main())

# 4782