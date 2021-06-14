a, b = input().split()
a, b = int(a), int(b)

def find_years(a, b):
    years = 0
    if a == b:
        return (years + 1)
    while a < b:
        a = a * 3
        b = b * 2
        years += 1
        if a == b:
            return (years + 1)
    return years

result = find_years(a, b)
print(result)