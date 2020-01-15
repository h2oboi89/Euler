#! python3

def main():
    s = 0

    for i in range(1000000):
        s_d = str(i)
        s_b = str(bin(i))[2:]

        if s_d == s_d[::-1] and s_b == s_b[::-1]:
            s += i

    return s

if __name__ == '__main__':
    print(main())

# 872187