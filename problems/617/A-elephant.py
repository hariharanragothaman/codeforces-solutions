def solve(friend_location):
    # elephant can jump 1, 2, 3, 4, 5
    cnt = 0
    while friend_location != 0:
        steps = friend_location // 5
        cnt += steps
        friend_location -= (steps * 5)
        # print("The updated friend location is:", friend_location)
        if friend_location == 0:
            return cnt

        steps = friend_location // 4
        cnt += steps
        friend_location -= (steps * 4)
        # print("The updated friend location is:", friend_location)
        if friend_location == 0:
            return cnt

        steps = friend_location // 3
        cnt += steps
        friend_location -= (steps * 3)
        # print("The updated friend location is:", friend_location)
        if friend_location == 0:
            return cnt

        steps = friend_location // 2
        cnt += steps
        friend_location -= (steps * 2)
        # print("The updated friend location is:", friend_location)
        if friend_location == 0:
            return cnt

        steps = friend_location // 1
        cnt += steps
        friend_location -= (steps * 1)
        # print("The updated friend location is:", friend_location)
        if friend_location == 0:
            return cnt


if __name__ == '__main__':
    friend_location = int(input())
    res = solve(friend_location)
    print(res)