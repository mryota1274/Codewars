def find_needle(haystack):
    # your code here
    for i in range(len(haystack)):
        #if  haystack[i] is not None:
            if haystack[i] == "needle":
                return "found the needle at position "+str(i)
