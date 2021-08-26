def solution(n):
    arr=[]
    for i in str(n):
        arr.append(int(i))
    arr.reverse()
    return arr

print(solution(57182))