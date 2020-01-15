#! python3

def champ(n):
    unlimited = False

    if n == -1:
        unlimited = True

    i = 1

    while True:
        for k in [int(j) for j in str(i)]:
            yield k

        i += 1

        if not unlimited and i == n:
            break

def main():
    i = 1
    j = 1
    p = 1

    while j < 1000001:
        for c in champ(-1):
            if j == i:
                p *= c
                i *= 10
            j += 1

            if j > 1000000:
                break

    return p

if __name__ == '__main__':
    print(main())

# 210