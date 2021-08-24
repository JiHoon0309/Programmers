def solution(s):
    a=s.split(" ")
    arr=[]
    for i in range(len(a)):
        for j in range(len(a[i])):
            if j%2==0:
                arr.append(a[i][j].upper())
            else:
                arr.append(a[i][j].lower())
        arr.append(' ')
    arr.pop()
    result="".join(arr)

    return result