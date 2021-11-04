def create_phone_number(n):
    #your code here
    n = [str(x) for x in n]
    return ("("+n[0]+n[1]+n[2]+")"+" "+n[3]+n[4]+n[5]+"-"+n[6]+n[7]+n[8]+n[9])
