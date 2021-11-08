def maskify(cc):
    maskcc = ''
    if len(cc) > 4:
        maskcc += '#' * (len(cc) - 4) + cc[-4:]
        return maskcc
    else:
     return cc
