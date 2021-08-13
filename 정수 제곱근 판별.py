import math

def solution(n):
    
    sqr=int(math.sqrt(n))
    if sqr**2==n:
        answer=(sqr+1)**2
    else:
        answer=-1

    return answer