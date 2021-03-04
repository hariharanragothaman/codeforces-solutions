n = int(input())
hash_map = {}

def reg(name):
    if name not in hash_map:
        hash_map[name] = 0
        return "OK"
    elif name in hash_map:
        hash_map[name] += 1
        return name + str(hash_map[name])


i = 0
while i < n:
    name = input()
    result = reg(name)
    print(result)
    i += 1