#! python3

def main():
    increase = 2
    s = 1
    limit = 1001 * 1001
    stop = False
    index = 0

    while True:
        for _ in range(1, 5):
            index += increase

            if index >= limit:
                stop = True
                break
            else:
                s += index + 1

        increase += 2

        if stop:
            break

    return s

if __name__ == '__main__':
    print(main())

# 669171001