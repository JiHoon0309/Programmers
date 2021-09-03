def solution(n):
    arr=[]
    for i in str(n):
        arr.append(i)
    arr.sort()
    arr.reverse()
    result=int(''.join(arr))
    return result