def solution(numbers):
    arr=[]
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            arr.append(numbers[i]+numbers[j])
    arr=list(set(arr))
    arr.sort()

    return arr