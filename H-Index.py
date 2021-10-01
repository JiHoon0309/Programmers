def solution(citations):
    citations.sort()
    count=0
    for i in range(len(citations)):
        if citations[i]>max(citations)//2:
            count+=1

    return count