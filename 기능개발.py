def solution(progresses, speeds):
    answer = []
    arr=[]
    c=1
    for i in range(len(progresses)):
        count=0
        while 100>progresses[i]:
            progresses[i]+=speeds[i]
            count+=1
        arr.append(count)
    temp=arr[0]
    for i in range(1,len(arr)):
        if temp>=arr[i]:
            c+=1
        else:
            temp=arr[i]
            answer.append(c)
            c=1
    answer.append(c)    
    return answer

print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))