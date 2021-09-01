def solution(progresses, speeds):
    answer = []
    arr=[]
    c=1
    temp=0
    for i in range(len(progresses)):
        count=0
        while 100>progresses[i]:
            progresses[i]+=speeds[i]
            count+=1
        arr.append(count)
    for i in arr:
        if arr[i]>arr[i+1]:
            temp=arr[i]
            


    answer.append(1)
    return answer