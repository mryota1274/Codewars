def get_middle(s):
    #your code here
    i = len(s)
    if i%2 == 0:
        return s[i//2-1:i//2+1]
    return s[i//2]
