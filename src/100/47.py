#! python3

from factorization import factor

def main():
    l = 4

    vals = []

    i = 0
    while True:
        f = factor(i)
        s = set(f)

        if len(s) == l:
            vals.append([i, f])
        else:
            vals = []

        if len(vals) == l:
            break

        i += 1

    return vals[0][0]

if __name__ == '__main__':
    print(main())

# 134043