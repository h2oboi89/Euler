#! python3

def get_range(power):
    i = 1

    while True:
        power_sum = i * 9 ** power

        if len(str(power_sum)) < i:
            return i - 1

        i += 1

    return 0

def main():
    answer = []

    power = 5

    num_digits = get_range(power)

    limit = ''

    for i in range(num_digits):
        limit += '9'

    limit = int(limit)

    for i in range(2, limit):

        power_sum = 0

        for c in str(i):
            power_sum += int(c) ** power

        if i == power_sum:
            answer.append(i)

    return sum(answer)

if __name__ == '__main__':
    print(main())

# 443839