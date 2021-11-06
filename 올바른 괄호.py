def solution(s):
    count1=0
    count2=0
    for i in s:
        if i=='(':
            count1+=1
        else:
            count2+=1
        if count1<count2:
            return False
    if count1!=count2:
        return False
    else:        
        return True
