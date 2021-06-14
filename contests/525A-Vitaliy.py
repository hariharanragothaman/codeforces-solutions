n = int(input())
rooms = input()

chars = 'abcdefghijklmnopqrstuvwxyz'
chars = [c for c in chars]
cnt = [0] * 26
hash_map = dict(zip(chars, cnt))
count = 0
i = 0

while i < len(rooms):
    if rooms[i] in hash_map:
        hash_map[rooms[i]] += 1
    elif rooms[i] not in hash_map and hash_map[rooms[i].lower()] > 0:
        hash_map[rooms[i].lower()] -= 1
    else:
        count += 1
    i += 1
print(count)