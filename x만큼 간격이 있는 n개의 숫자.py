def solution(x, n):
    arr=[]
    sum=x
    for i in range(n):
        arr.append(sum)
        sum+=x
    return arr