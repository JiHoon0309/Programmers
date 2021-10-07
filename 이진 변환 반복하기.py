def solution(s):
    count=0
    count1=0
    
    while s!='1':
        count+=1
        count2=len(s)
        count1+=s.count('0')   #제거할 0의 개수
        count2-=s.count('0')   #0 제거 후 길이
        s=bin(count2)[2:]

    return [count, count1]        


print(solution("01110"))
