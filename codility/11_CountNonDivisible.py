# https://www.youtube.com/watch?v=tImgeYTHdAU
import math

def solution(A):
    """
    3 1 2 3 6
      3 3   
             
    2 2   2  
      3 3   
    6 6 6 6  
    """

    n = len(A)
    count = {}

    for a in A:
        count[a] = count.get(a, 0) + 1
    
    A_ans = {a: 0 for a in A}
    
    for a in A_ans:
        s = 0
        for div in range(1, int(math.sqrt(a)) + 1):
            if a % div == 0:
                s += count.get(div, 0)
                if int(a / div) != div:
                    s += count.get(int(a / div), 0)
        A_ans[a] = n - s
    
    ans = []
    for a in A:
        ans.append(A_ans[a])
    return ans


