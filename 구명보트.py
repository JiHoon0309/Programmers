def solution(people, limit):
    people.sort()
    sum=0
    count=0
    i=1
    sum=people[0]+people[len(people)-1]
    while True:
        if people[0]==(limit//2) and people.count(limit//2)==1:
            count+=1
            people.remove(people[0])

        if people[0]>limit//2:
            count+=len(people)
            break

        if sum>limit:
            sum=people[0]+people[len(people)-1-i]
            i+=1
        if sum==100:
            people.remove(people[len(people)-i])
            people.remove(people[0])
            count+=1
        if len(people)-i==1:
            people.remove(people[0])

    return count
print(solution([70, 50, 80, 30]	,100))
