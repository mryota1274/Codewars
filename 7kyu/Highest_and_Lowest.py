def high_and_low(numbers):
    # ...
    strlist = numbers.split(' ')
    numlist = list(map(int,strlist))
    maxnum = str(max(numlist))
    minnum = str(min(numlist))
    
    return maxnum+" "+minnum
