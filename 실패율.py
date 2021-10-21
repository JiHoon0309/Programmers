def solution(N, stages):
    result=[]
    count3=0
    for i in range(1,N+1):
        count=0
        count2=0
        for j in range(len(stages)):
            if stages[j]>=i:
                count+=1
            if stages[j]==i:
                count2+=1
        count3+=1
        result.append([count2/count,count3])
    result.sort(reverse=True, key=lambda x:x[0])
    for i in range(len(result)):
        result[i].pop(0)
    answer=sum(result,[])
    return answer