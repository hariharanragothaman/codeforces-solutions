"""
n -> n / 2
n -> 2n / 3
n -> 4n / 5

"""
"""
initial thoughts
a. As we thought this is a greedy question


"""

def number_of_moves(n):
    moves = 0
    if n == 1: return 0

    while n != 1:
        if n == 1:
            break
        elif n % 5 == 0:
            n = 4*n // 5
            moves += 1
        elif n % 3 == 0:
            n = 2*n // 3
            moves += 1
        elif n % 2 == 0:
            n = n // 2
            moves += 1
        else:
            break
    
    if n == 1:
        return moves
    else:
        return -1


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        op =  number_of_moves(n)
        print("The op is:", op)
        t -= 1    