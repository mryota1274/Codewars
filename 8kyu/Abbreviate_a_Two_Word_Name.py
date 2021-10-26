def abbrev_name(name):
    namelist = name.split(" ")
    Fname = namelist[0][0].upper()
    Lname = namelist[1][0].upper()
    return Fname+"."+Lname
