def solution(sizes):
    maxNum=[]
    minNum=[]
    for i in range(len(sizes)):
        maxNum.append(max(sizes[i]))
        minNum.append(min(sizes[i]))
        
    result=max(maxNum)*max(minNum)
    return result

print(solution([[60, 50], [30, 70],
 [60, 30], [80, 40]]))