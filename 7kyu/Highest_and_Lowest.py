def high_and_low(numbers):
    # ...
    strlist = numbers.split(' ')
    numlist = list(map(int,strlist))
    return str(max(numlist)) + " " + str(min(numlist))
