def solution(s):
    list1=list(map(int, s.split()))
    list1.sort()
    answer=[]
    answer.append(list1[0])
    answer.append(list1[-1])
    answer=list(map(str,answer))
    result=" ".join(answer)
    return result