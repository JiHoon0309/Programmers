def solution(s):
    if s[0]=='(' and s[-1]==')' and s.count('(')==s.count(')'):
        return True
    else:
        return False