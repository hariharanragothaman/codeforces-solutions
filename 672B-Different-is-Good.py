"""
Idea is if we want to make all substrings not equal - then if the string length is > 27 - not possible
else - we know the minimum number of changes as follows

"""
n=int(input())
print(n-len(set(input())) if n<27 else -1)