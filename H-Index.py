def solution(citations):
    citations.sort()
    result=0
    answer=[]

    if citations[0]>len(citations):
        result=len(citations)
    elif citations[0]>0 and citations[0]>len(citations):
        result=citations[0]
    else:
        for i in range(len(citations)):
            count=0
            for j in citations:
                if i<=j:
                    count+=1
            if i<=count:
                answer.append(i)
        result=max(answer)

    return result