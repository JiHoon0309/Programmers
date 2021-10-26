import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    count=0
    if scoville[0]>=K:
        return -1
    while len(scoville)>=2:
        if scoville[0]>=K:
            break
        count+=1
        scoville_min=heapq.heappop(scoville)
        scoville_min2=heapq.heappop(scoville)
        new=scoville_min+(scoville_min2*2)
        heapq.heappush(scoville, new)
    if max(scoville)<K:
        return -1
    return count