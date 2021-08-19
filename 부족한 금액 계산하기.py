def solution(price, money, count):
    sum=0
    i=0
    temp=0
    for i in range(count):
        temp=price
        i+=1
        temp*=i
        sum+=temp
        answer=sum-money
    if answer<0:
        return 0
    return answer