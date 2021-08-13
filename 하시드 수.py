def solution(x):
    x_1=int(x/10000)
    x_2=int(x/1000)
    x_3=int((x%1000)/100)
    x_4=int((x%100)/10)
    x_5=int((x%10))
    arr=[x_1,x_2,x_3,x_4,x_5]
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
    if x%sum==0:
        return True
    else:
        return False