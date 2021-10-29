def square_digits(num):
    num = str(num)
    listnum = list(num)
    listnum = [int(s) for s in listnum]
    listn = []
    for i in listnum:
        listn.append(i**2)

    numstr = ""

    for i in listn:
        numstr = numstr+str(i)

    return  int(numstr)
