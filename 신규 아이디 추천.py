import re
def solution(new_id):
    new_id=new_id.lower()   #1단계
    
    new_id=re.sub('[^A-Za-z0-9\-\_\.]','',new_id)   #2단계

    while '..' in new_id:   #3단계
        new_id=new_id.replace('..','.')

    new_id=new_id.strip('.')  #4단계

    if len(new_id)==0:  #5단계
        new_id='a'

    if len(new_id)>=16:  #6단계
        new_id=new_id[:15]
        if new_id[-1]=='.':
            new_id=new_id.rstrip('.')#마침표 제거
    
    if len(new_id)<=2:   #7단계
        while len(new_id)<3:
            new_id=new_id+new_id[-1]

    return new_id