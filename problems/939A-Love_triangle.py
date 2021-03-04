N = int(input())
arr = input().split()
arr = [int(c) for c in arr]

# Adding a zero in-front was a smart thing to do here.
arr = [0] + arr

flag = False
for i in range(1, N+1):
    if arr[arr[arr[i]]] == i:
        flag = True
if flag:
    print("YES")
else:
    print("NO")