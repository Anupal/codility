

def check_meet(f1, f2):
    return f1 == 1 and f2 == 0

def solution(A, B):
    """
    4 3 2 1 5
    0 1 0 0 0
    < > < < <

    < >
    > < *
    < <
    > >

    > > >     <
              >
    """
    # fish away dir, add to stack
    # fish facing dir, keep popping and comparing while facing dir
    n, stack = len(A), []
    for i in range(n):
        ignore = False
        while stack and check_meet(stack[-1][1], B[i]):
            if stack[-1][0] < A[i]:
                stack.pop()
            else:
                ignore = True
                break

        if not ignore:
            stack.append((A[i], B[i]))

    return len(stack)


