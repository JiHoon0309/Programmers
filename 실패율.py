def solution(N, stages):
    stages.sort()
    i=1
    list1=[]
    length=len(stages)
    sum=0
    while i<=N:
        if len(stages)==0:
            list1.append(sum/length)
            break
        if stages[0]==i:
            sum+=1
            stages.pop(0)
        else:
            list1.append(sum/length)
            i+=1
            sum=0 

    return list1

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
