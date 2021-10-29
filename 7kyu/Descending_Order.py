def descending_order(num):
    # Bust a move right here
    num=str(num)
    num=list(num)
    numlist = [int(s) for s in num]
    list.sort(numlist, reverse=True)
    n = int("".join(map(str,numlist)))
    return n
    
