#! python3

import itertools

def main():
    perms = list(itertools.permutations(list(range(10))))

    return int(''.join(map(str, perms[999999])))

if __name__ == '__main__':
    print(main())

# 2783915460