number_of_rooms = 0
tests = int(input())

while tests > 0:
    p, q = input().split()
    p, q = int(p), int(q)
    if q - p >= 2:
        number_of_rooms += 1
    tests -= 1

print(number_of_rooms)