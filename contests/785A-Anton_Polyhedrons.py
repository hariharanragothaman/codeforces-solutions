hash_map = { "Tetrahedron" : 4,
             "Cube" : 6,
             "Octahedron": 8,
             "Dodecahedron": 12,
             "Icosahedron":20
}

N = int(input())
i = 0
total = 0
while i < N:
    total += hash_map[input()]
    i += 1
print(total)