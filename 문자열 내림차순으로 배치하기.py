def solution(s):
    arr=[]
    for i in s:
        arr.append(i)
    arr.sort()
    arr.reverse()

    result=''.join(arr)
    return result