from collections import deque

def find_min_jumps(cords, total, max_distance):
    """
    1.Basically you know the starting point - try to jump maximum up to max_dist
    2. If not able to jump max_dist, then try to jump as much as possible
       within - max_dist - How do I find that? - DFS.
    3. Increment the count as you jump.
    """
    left, count = 0
    for i in range(len(cords)):



if __name__ == '__main__':
    n, d = map(int, input().split())
    axis = input()
    find_min_jumps(axis, n, d)