def solution(table, languages, preference):
    string=" ".join(table)
    arr=string.split(' ')
    arr2=[]
    result=[]
    for i in range(len(table)):
        a=[]
        for j in range(i*6,(i+1)*6):
            a.append(arr[j])
        arr2.append(a)
    for i in range(len(arr2)):
        score=0
        for j in range(1,len(arr2[i])):
            for z in range(len(languages)):
                if arr2[i][j]==languages[z]:
                    score+=(6-j)*preference[z]
        result.append(score)


    return arr2[result.index(max(result))][0]