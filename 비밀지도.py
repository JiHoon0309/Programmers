def solution(n, arr1, arr2):
    result=[]
    for i in range(len(arr1)):
        answer=''
        bin=arr1[i]|arr2[i]
        for _ in range(len(arr1)):
            if bin%2==1:
                answer='#'+answer
            else:
                answer=' '+answer
            bin=bin//2
        result.append(answer)

    return result