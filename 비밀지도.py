def solution(n, arr1, arr2):
    map1=[]
    map2=[]
    result=[]
    answer=[]
    for i in range(n):
        binary1=(format(arr1[i],'b'))
        binary2=(format(arr2[i],'b'))
        if len(binary1)<n:
            binary1=(str(binary1).zfill(n))
        if len(binary2)<n:
            binary2=(str(binary2).zfill(n))
        map1.append(binary1)
        map2.append(binary2)
    for i in range(n):
        for j in range(n):
            if map1[i][j]=='1' or map2[i][j]=='1':
                result.append('#')
            elif map1[i][j]=='0' and map2[i][j]=='0':
                result.append(' ')
    String="".join(result)
    for i in range(0,len(String),n):
        c=(String[i:i+n])
        answer.append(c)

    return answer