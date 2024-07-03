def solution(S, P, Q):
    """
    2D matrix to store the next occurence of nucleotide
    for a given index
    """
    n, nmap = len(S), {"A": 1, "C": 2, "G": 3, "T": 4}
    
    # storage
    nt = [[-1] * n, [-1] * n, [-1] * n, [-1] * n]
    last_seen = [-1] * 4
    for i in range(n - 1, -1, -1):
        last_seen[nmap[S[i]] - 1] = i
        for k in range(4):
            if last_seen[k] != -1:
                nt[k][i] = last_seen[k]

    # execute queries
    # next occurence should be before j
    ans = []
    for k in range(len(P)):
        i = P[k]
        j = Q[k]
        # A
        if 0 <= nt[0][i] <= j:
            ans.append(1)
        # C
        elif 0 <= nt[1][i] <= j:
            ans.append(2)
        # G
        elif 0 <= nt[2][i] <= j:
            ans.append(3)
        # T
        else:
            ans.append(4)

    return ans
