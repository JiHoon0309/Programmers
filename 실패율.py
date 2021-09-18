def solution(N, stages):
    result=[]
    for i in range(1,N+1):
        count=0
        count2=0
        for j in range(len(stages)):
            if stages[j]>=i:
                count+=1
            if stages[j]==i:
                count2+=1
        result.append(count2/count)
        
    return result

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))