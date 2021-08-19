def solution(s):
    str=s
    if len(str)%2==0:
        a=len(str)//2
        return str[a-1]+str[a]
    else:
        b=len(str)//2
        return str[b]