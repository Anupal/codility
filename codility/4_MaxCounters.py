def solution(N, A):
    """
    lazy update values with last max
    """
    counters = [0] * N

    last_max, current_max = 0, 0
    for a in A:
        if a == N + 1:
            last_max = current_max
        else:
            # check if last_max has been added
            if counters[a - 1] < last_max:
                counters[a - 1] = last_max
            
            # normal increment
            counters[a - 1] += 1
            
            # update current max
            current_max = max(current_max, counters[a - 1])
    
    # finally update all remaining counters with last max
    for i in range(N):
        if counters[i] < last_max:
            counters[i] = last_max
        
    return counters
