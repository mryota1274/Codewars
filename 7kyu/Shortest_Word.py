def find_short(s):
    # your code here
    l = s.split(" ")
    return len(min(l, key=len)) # l: shortest word length
