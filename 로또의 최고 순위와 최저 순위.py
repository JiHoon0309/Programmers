def solution(lottos, win_nums):
    min=0
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            min+=1
    max=min
    for i in range(len(lottos)):
        if lottos[i]==0:
            max+=1

    rank={6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}

    return [rank[max],rank[min]]