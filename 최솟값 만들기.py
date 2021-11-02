def solution(A,B):
    result=0
    A.sort()
    B.sort()
    for i in range(len(A)):
        result+=A[0]*B[-1]
        A.pop(0)
        B.pop()
    return result