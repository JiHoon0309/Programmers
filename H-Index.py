def solution(citations):
    citations.sort()
    result=0
    if len(citations)<citations[0]:
        result==len(citations)
    else:
        for i in range(len(citations)):
            up=0
            down=0
            for j in citations:
                if i<j:
                    up+=1
                elif i>j:
                    down+=1
                elif i==j:
                    up+=1
                    down+=1
            if i==up:
                result=up
    return result

