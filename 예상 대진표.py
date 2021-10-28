import math
def solution(n,a,b):
    count=1
    temp=0
    if a>b:
        temp=a
        a=b
        b=temp
    while n>=2:
        if a==0:
            a+=1
        if b%2==0 and b-a==1:
            break
        else:
            count+=1
            a=math.ceil(a/2)
            b=math.ceil(b/2)

    return count
