def solution(arr1, arr2):
    sum=[]
    for i in range(len(arr1)):
        a=[]
        for j in range(len(arr2[0])):
            a.append(arr1[i][j]+arr2[i][j])
        sum.append(a)
    return sum