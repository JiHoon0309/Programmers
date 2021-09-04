def solution(n):
    arr=[]
    result=0
    while n>0:
        a=n%3
        n=n//3
        arr.append(a)
    for i in range(len(arr)):
        if arr[i]==0:
            pass
        else:
            result+=(arr[i]*(3**(len(arr)-i-1)))
    return result