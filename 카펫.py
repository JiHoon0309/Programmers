def solution(brown, yellow):
    sum=brown+yellow
    list=[]
    for i in range(1,sum+1):
        if sum%i==0:
            list.append(i)
    if len(list)%2==0:
        return list[len(list)//2],list[(len(list)//2)-1]
    else:
        return list[len(list)//2],list[len(list)//2]