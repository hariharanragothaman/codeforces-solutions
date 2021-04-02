def calculate_distance(g, gold):
    """
    Given an array - find the shortest sub-array the adds up to the target
    Technique to use her is sliding window.
    :return: sum of the shortest subarray
    """
    left, right, total = 0, 0, 0
    min_length = float('inf')

    for i in range(len(g)):
        right = i
        total += g[i]
        print("The total is:", total)

        while total >= gold:
            # Whenever we have a total - greater we need to calculate the min_ length
            min_length = min(right - left + 1, min_length)
            print("Contracting the window")
            total -= g[left]   # We also have to reduce first and then increment the right pointer.
            left += 1
            print("The total is:", total)

        print("The left & right are:", left, right)
        print("The min length is:", min_length)
        print("The total is:", total)
        print("*********************")

    if min_length != float('inf'):
        return min_length
    else:
        return -1


if __name__ == '__main__':
    n, gold = input().split()
    gold = int(gold)
    g = input().split()
    g = [int(c) for c in g]
    op = calculate_distance(g, gold)
    print(op)