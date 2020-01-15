#! python3

from permute import permute
from enum import Enum

def parseInt(digits):
    val = 0
    multiplier = 1

    for d in digits[::-1]:
        val += (d * multiplier)
        multiplier *= 10

    return val

class Mode(Enum):
    OneFour = 1
    TwoThree = 2

def permuteNumbers(digits, mode):
    if mode == Mode.OneFour:
        m = 1
    elif mode == Mode.TwoThree:
        m = 2

    e = 5

    a = parseInt(digits[0:m])
    b = parseInt(digits[m:e])
    c = parseInt(digits[e:])

    return a, b, c

def main():
    limit = 9

    vals = list(range(1, limit + 1))
    sums = set()
    modes = [Mode.OneFour, Mode.TwoThree]

    for p in permute(vals):
        # only need to check 1 digit * 4 digit and 2 digit * 3 digits

        for mode in modes:
            a, b, c = permuteNumbers(p, mode)

            if a * b == c:
                if not c in sums:
                    sums.add(c)

    return sum(sums)

if __name__ == '__main__':
    print(main())

# 45228