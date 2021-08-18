def solution(a, b):
    sum=0
    temp=0
    for i in range(len(a)):
        sum=a[i]*b[i]
        temp+=sum
    return temp