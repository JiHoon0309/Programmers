def solution(n, lost, reserve):
    setlost=set(lost)
    setreserve=set(reserve)
    settemp1=set()
    settemp2=set()

    setlost-=setreserve #본인 체육복 잃어버려서 본인꺼 입음
    
    
    for i in setlost:   
        if i+1 in setreserve:
            settemp1.add(i)
            settemp2.add(i+1)
    setlost-=settemp1
    setreserve-=settemp2  #뒷번호 체육복 빌림

    for i in setlost:    
        if i-1 in setreserve:
            settemp1.add(i)
            settemp2.add(i-1)
    setlost-=settemp1
    setreserve-=settemp2  #앞번호 체육복 빌림

        
    return n-len(setlost)


print(solution(	5, [1,2,3,4,5], [3,5]))
