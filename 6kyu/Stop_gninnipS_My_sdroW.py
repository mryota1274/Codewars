def spin_words(sentence):
    # Your code goes here
    l = sentence.split(" ")
    for x in range(len(l)):
        if len(l[x])>=5:
            l[x] = l[x][::-1]
    return " ".join(l)
