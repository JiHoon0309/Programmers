def solution(answers):
    person_1=[1,2,3,4,5]
    person_2=[2,1,2,3,2,4,2,5]
    person_3=[3,3,1,1,2,2,4,4,5,5]
    count1=0
    count2=0
    count3=0
    result=[]
    answer=[]
    for i in range(len(answers)):
        if answers[i]==person_1[i%5]:
            count1+=1
        if answers[i]==person_2[i%8]:
            count2+=1
        if answers[i]==person_3[i%10]:
            count3+=1
    result=[count1,count2,count3]
    maxPerson=max(result)
    for i in range(len(result)):
        if result[i]==maxPerson:
            answer.append(i+1)
    return answer