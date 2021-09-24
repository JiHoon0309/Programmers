def solution(n, lost, reserve):
    setlost=set(lost)-set(reserve)
    setreserve=set(reserve)-set(lost) #본인 중복 제외

    for i in setreserve:
        if i-1 in setlost:
            setlost.remove(i-1)   #앞번호 없을떄 빌려주고 앞번호 제외
        elif i+1 in setlost:
            setlost.remove(i+1)   #뒷번호 없을때 빌려주고 뒷번호 제외
    
    return n-len(setlost)