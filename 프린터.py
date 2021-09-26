def solution(priorities, location):
    order=max(priorities)                       #가장큰값
    count=0                                     #몇번째 출력인가?

    while len(priorities)>0:                    #priorities의 길이가 0보다 클경우 반복
        if priorities[0]!=order:                #만약 맨앞숫자가 가장큰 값이 아닌경우
            priorities.append(priorities[0])    #맨앞 숫자를 맨뒤에 추가
            priorities.remove(priorities[0])    #맨앞 숫자를 제거
            location-=1                         #location를 앞으로 한자리 옮김
        
        if location==-1:                        #만약 location이 -1인경우
            location=len(priorities)-1          #맨뒤로 옮김
        
        if priorities[0]==order:                #만약 맨앞 숫자가 가장큰 값인경우
            priorities.remove(priorities[0])    #가장큰 숫자 제거
            if len(priorities)>0:                   #만약 priorities 의 길이가 0이상일경우
                order=max(priorities)               #가장큰 숫자 새로 정함
            count+=1                            #몇번째로 출력인지 정함
            location-=1                         #location을 앞으로 한자리 옮김(맨앞에 숫자를 뺏기 때문에)
        
        if location==-1:                        #맨앞에서 빠졌을 경우
            break                               #멈춤

    return count