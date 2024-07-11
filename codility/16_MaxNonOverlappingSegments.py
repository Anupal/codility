# https://codesays.com/2015/solution-to-max-nonoverlapping-segments-by-codility/

def solution(A, B):
    """
    a cluster is segments which overlap with each other
    we need to find maximum number of non-overlapping segments
    if we have 3 clusters
    then we can take 1 segment each from cluster to get 3 
    non-overlapping segments.
    therefore we only need to find number of clusters
    """

    n, clusters, i = len(A), 0, 0
    

    while i < n:
        # start a cluster
        j = i + 1
        
        # increment j while it is part of cluster
        while j < n:
            if A[j] > B[i]:
                break    
            j += 1
        # end the cluster
        i = j
        clusters += 1
    
    return clusters
