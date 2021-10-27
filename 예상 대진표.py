def solution(n,a,b):
    count=1
    while n>2:
        if a<=n//2 and b>n//2:
            count+=1
            b=round(b/2)
            a=round(a/2)
            n=n//2
        else:
            return count
    return count