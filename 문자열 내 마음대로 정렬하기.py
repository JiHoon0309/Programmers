def solution(strings, n):

    order=[]
    result=[]
    answer=[]
    for i in range(len(strings)):
        order.append(strings[i][n])
        result.append(order[i]+strings[i])
    result.sort()
    for j in range(len(strings)):
        answer.append(result[j][1:])
    return answer

print(solution(["sun", "bed", "car"],1))