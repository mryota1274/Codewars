def accum(s):
    # your code
    return "-".join([(s[x] * (x+1)).capitalize() for x in range(len(s))])
