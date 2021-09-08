def solution(scores):
    result=[]
    scores_sum=[]
    for i in range(len(scores)):
        a=[]
        for j in range(len(scores)):
            a.append(scores[j][i])
        result.append(a)
    
    for i in range(len(result)):
        
        if result[i][i] and (result[i][i]==max(result[i]) or result[i][i]==min(result[i])):
            result[i].remove(result[i][i])
        scores_sum.append(sum(result[i])/len(result[i]))


        if scores_sum[i]>=90:
            scores_sum[i]='A'
        elif 80<=scores_sum[i]<90:
            scores_sum[i]='B'
        elif 70<=scores_sum[i]<80:
            scores_sum[i]='C'
        elif 50<=scores_sum[i]<70:
            scores_sum[i]='D'
        else:
            scores_sum[i]='F'

    return ''.join(scores_sum)

print(solution([[100,90,98,88,65],
                [50,45,99,85,77],
                [47,88,95,80,67],
                [61,57,100,80,65],
                [24,90,94,75,65]]))