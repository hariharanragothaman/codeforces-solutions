def find_num_shovels(cost, change):
    for i in range(1, 10000):
        if (i * cost) % 10 == 0:
            print(i)
            return
        elif ((i * cost) - change) % 10 == 0:
            print(i)
            return


if __name__ == '__main__':
    cost, change = map(int, input().split())
    find_num_shovels(cost, change)