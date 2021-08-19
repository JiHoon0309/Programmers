def solution(n):
    a=str(n)
    arr=list(a)
    sum=0
    for i in range(len(arr)):
        sum+=int(arr[i])

    return sum