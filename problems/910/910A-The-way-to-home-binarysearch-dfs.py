
import bisect

def the_way_to_home(s, n, d):
    one_index = [int(i+1) for i, c in enumerate(s) if c == '1']

    i = 0
    jmpcnt = 0

    while i < len(one_index):

        if i == len(one_index) - 1:
            break

        mx_jump = one_index[i] + d

        if mx_jump in one_index:
            jmpcnt += 1
            i = one_index.index(mx_jump)

        elif mx_jump not in one_index:
            # We need to find closest value < than mx_jump
            index = bisect.bisect(one_index, mx_jump)

            # Check if we are not being stagnant
            if i != index -1:
                i = index - 1
            else:
                break

            jmpcnt += 1

    if jmpcnt and i == len(one_index)-1:
        print(jmpcnt)
    else:
        print("-1")




if __name__ == '__main__':
    n, d = map(int, input().split())
    s = input()
    the_way_to_home(s, n, d)







