def solution(nums):
    
    choice=len(nums)//2
    set1=len(set(nums))
    if choice>set1:
        result=set1
    else:
        result=choice
    return result