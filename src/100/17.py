#! python3

def convert(n):
    t = ''
    h = ''
    w = ''

    a = n % 1000

    b = a % 100

    w = convert_helper(b)

    n = (n - a) // 1000

    if n > 0:
        t = convert(n) + 'thousand'

    a = (a - b) // 100

    if a > 0:
        h = convert(a) + 'hundred'

        if len(w) > 0:
            h = h + 'and' + w

        w = h

    return t + w

def convert_helper(n):
    w = ''

    if n < 20:
        if n == 1:
            w = 'one'
        if n == 2:
            w = 'two'
        if n == 3:
            w = 'three'
        if n == 4:
            w = 'four'
        if n == 5:
            w = 'five'
        if n == 6:
            w = 'six'
        if n == 7:
            w = 'seven'
        if n == 8:
            w = 'eight'
        if n == 9:
            w = 'nine'
        if n == 10:
            w = 'ten'
        if n == 11:
            w = 'eleven'
        if n == 12:
            w = 'twelve'
        if n == 13:
            w = 'thirteen'
        if n == 14:
            w = 'fourteen'
        if n == 15:
            w = 'fifteen'
        if n == 16:
            w = 'sixteen'
        if n == 17:
            w = 'seventeen'
        if n == 18:
            w = 'eighteen'
        if n == 19:
            w = 'nineteen'
    else:
        d = n % 10

        n = n - d

        if n == 20:
            w = 'twenty'
        if n == 30:
            w = 'thirty'
        if n == 40:
            w = 'forty'
        if n == 50:
            w = 'fifty'
        if n == 60:
            w = 'sixty'
        if n == 70:
            w = 'seventy'
        if n == 80:
            w = 'eighty'
        if n == 90:
            w = 'ninety'

        w = w + convert(d)

    return w

def main():
    return sum(map(len, map(convert, range(1001))))

if __name__ == '__main__':
    print(main())

# 21124