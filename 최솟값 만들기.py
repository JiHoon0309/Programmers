def solution(A,B):
    result=0
    for i in range(len(A)):
        minn=min(A)
        maxx=max(B)
        result+=minn*maxx
        A.remove(minn)
        B.remove(maxx)
    return result