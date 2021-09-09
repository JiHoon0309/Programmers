def solution(scores):
    result=[]
    scores_sum=[]
    temp=0
    for i in range(len(scores)):
        a=[]
        for j in range(len(scores)):
            a.append(scores[j][i])
        result.append(a)
    
    for i in range(len(result)):
        if (result[i][i]==max(result[i]) or result[i][i]==min(result[i])):
            temp=result[i][i]
            result[i].remove(result[i][i])
        if temp in result[i]:
            result[i].append(temp)
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