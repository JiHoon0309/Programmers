def solution(s):
    s=s.lower()
    count_1=0
    count_2=0
    for i in range(len(s)):
        if s[i]=='p':
            count_1+=1
        elif s[i]=='y':
            count_2+=1
            
    if count_1==count_2:
        return True
    else:
        return False