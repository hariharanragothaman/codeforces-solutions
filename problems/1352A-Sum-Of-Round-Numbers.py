def sum_of_round_numbers(num):
    res = []
    num = str(num)
    j = len(num) - 1
    for i in range(len(num)):
        temp = int(num[i]) * (10**j)
        if temp:
            res.append(temp)
        j -= 1
    return res


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        res = sum_of_round_numbers(n)
        print(len(res))
        print(*res)
        t -= 1