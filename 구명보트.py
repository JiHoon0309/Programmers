def solution(people, limit):
    people.sort()
    count=0
    while len(people)>0:
        sum=people[0]+people[-1]
        if sum<=limit:
            count+=1
            people.pop()
            people.pop(0)
        else:
            people.pop()
            count+=1
        if len(people)==1:
            count+=1
            break
    return count

print(solution([70, 80, 50]	,100))
