# https://codesays.com/2014/solution-to-sigma-2012-stone-wall-by-codility/

def solution(H):
    N = len(H)
    stones, stack = 0, []

    for i in range(N):
        # height low - blocks end here
        while stack and H[i] < stack[-1]:
            stack.pop()

        # height high - new block
        if not stack or H[i] > stack[-1]:
            stack.append(H[i])
            stones += 1

        # height same - do nothing

    return stones

