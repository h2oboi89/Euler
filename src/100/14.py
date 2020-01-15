#! python3


def main():
    chain = []

    for i in range(1, 1000000):
        c = []

        while True:
            c.append(i)

            if i == 1:
                break

            if i % 2 == 0:
                i = i // 2
            else:
                i = 3 * i + 1

        if len(c) > len(chain):
            chain = c

    return chain[0]

if __name__ == '__main__':
    print(main())

# 837799