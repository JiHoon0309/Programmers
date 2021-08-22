def solution(left, right):
    arr=[]
    for i in range(left,right+1):
        count=0
        for j in range(i):
            if i%(j+1)==0:
                count+=1
        if count%2==0:
            arr.append(i)
        else:
            arr.append(-i)
    return sum(arr)