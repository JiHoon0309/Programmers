def solution(N, stages):
    dic={}
    total=len(stages)

    for i in range(1,N+1):
        if total!=0:
            now=stages.count(i)
            rate=now/total
            dic[i]=rate
            total-=now
        else:
            dic[i]=0
    
    return sorted(dic, key=lambda x: dic[x], reverse=True)
