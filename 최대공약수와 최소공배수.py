def solution(n, m):
    c=1
    a=max(n,m)
    b=min(n,m)
    while c>0:
        
        c=a%b
        a=b
        b=c
    
    result=[a,(m*n)//a]
    return result