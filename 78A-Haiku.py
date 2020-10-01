print(['NO', "YES"][[sum(c in "aeiou" for c in input()) for _ in range(3)] == [5, 7, 5]])
