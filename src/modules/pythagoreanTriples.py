def sortA(val):
    return val[0]


def tripletsWithSum(sum):
    results = []

    m = 2

    while(m * m < sum / 2):
        n = 1

        while(n < m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n

            for i in range(1, sum):
                a_i = a * i
                b_i = b * i
                c_i = c * i

                s = a_i + b_i + c_i

                if s > sum:
                    break

                if s == sum:
                    t = [a_i, b_i, c_i]

                    t.sort()

                    if t not in results:
                        results.append(t)

            n += 1

        m += 1

    results.sort(key=sortA)

    return results
