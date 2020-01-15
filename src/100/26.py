#! python3

def main():
    sequence_length = 0
    n = 0

    for i in range(1000, 1, -1):
        if sequence_length >= i:
            break

        remainders = []
        for _ in range(i):
            remainders.append(0)

        v = 1
        p = 0

        while remainders[v] == 0 and v != 0:
            remainders[v] = p
            v *= 10
            v %= i
            p += 1

        if p - remainders[v] > sequence_length:
            n = i
            sequence_length = p - remainders[v]

    return n

if __name__ == '__main__':
    print(main())

# 983