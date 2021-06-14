N = int(input())
results = input()

if results.count('A') > results.count('D'):
    print("Anton")
elif results.count('D') > results.count('A'):
    print("Danik")
else:
    print("Friendship")