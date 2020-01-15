#! python3

# find the number of ways to reach a total with the given number of combinations
def nway(total, coins):
    if not coins:
        return 0

    c, coins = coins[0], coins[1:]
    count = 0

    if total % c == 0:
        count += 1

    for amount in range( 0, total, c):
        count += nway(total - amount, coins)

    return count

def main():
    return nway(200, [1,2,5,10,20,50,100,200])

if __name__ == '__main__':
    print(main())

# 73682