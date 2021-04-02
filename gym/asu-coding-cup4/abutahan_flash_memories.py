def calculate_need(solns, solns_size, mem_size):
    total_capacity = solns_size * solns
    one_store = mem_size // solns_size
    # In one basket you can store this much?
    #print(one_store)
    one_capacity = solns_size * one_store
    #print(one_capacity)
    q, r  = divmod(total_capacity, one_capacity)
    #print(q, r)
    if r:
        return q + 1
    else:
        return q


if __name__ == '__main__':
    nfiles, file_size, capacity = list(map(int, input().split()))
    op = calculate_need(nfiles, file_size, capacity)
    print(op)