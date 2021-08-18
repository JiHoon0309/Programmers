def solution(a, b):
    sum=0
    if a<b:
        for i in range(b-a+1):
            sum=sum+a+i
    else:
        for i in range(a-b+1):
            sum=sum+b+i
        
    return sum