#! python3

from math import floor

def day_of_week(year, month, day):
    month -= 2 # march = 1

    if (month <= 0):
        month += 12 # january = 11, february = 12
        year -= 1

    d = year % 100
    century = (year - d) // 100

    a = floor((13 * month - 1) / 5)
    b = floor(d / 4)
    c = floor(century / 4)

    return (day + a + d + b + c - 2 * century) % 7

def main():
    c = 0

    for year in range(1901, 2001):
        for month in range(12):
            if day_of_week(year, month + 1, 1) == 0:
                c += 1

    return c

def test():
    answer = main()
    print(answer)
    return answer == 171

if __name__ == '__main__':
    print(main())
