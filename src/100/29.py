#! python3

def main():
    s = set()

    limit = 100

    for a in range(2, limit + 1):
        for b in range(2, limit + 1):
            s.add(a ** b)

    return len(s)

if __name__ == '__main__':
    print(main())

# 9183