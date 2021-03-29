
def soldier_and_bananas(cost_of_first, dollars, number_of_bananas_needed):
    cost = [0] * number_of_bananas_needed
    for i in range(len(cost)):
        cost[i] = (i+1) * cost_of_first
    rem = dollars - sum(cost)
    if rem < 0:
        print(abs(rem))
    else:
        print(0)



if __name__ == '__main__':
    k, n, w = list(map(int, input().split()))
    soldier_and_bananas(k, n, w)
