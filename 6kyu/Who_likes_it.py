def likes(names):
    # your code here
    if not names:
        return 'no one likes this'
    if len(names)>=4:
        return names[0]+", "+names[1]+" and "+str(len(names)-2)+" others like this"
    if len(names)==3:
        return names[0]+", "+names[1]+" and "+names[2]+" like this"
    if len(names)==2:
         return names[0]+" and "+names[1]+" like this"
    if len(names)==1:
        return((", ".join(names)) + ' likes this')
    
