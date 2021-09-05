def solution(strings, n):
    arr=[]
    a=0
    for i in strings:
        if i==' ':
            arr.append(chr(ord(i)))

        elif 65<=ord(i)<=90:
            if ord(i)+n>=91:
                a=ord(i)+n-91+65
                arr.append(chr(a))
            else:
                arr.append(chr(ord(i)+n))
            
        elif 97<=ord(i)<=122:
            if ord(i)+n>=123:
                a=ord(i)+n-123+97
                arr.append(chr(a))
            else:
                arr.append(chr(ord(i)+n))

    return "".join(arr)