def get_count(sentence):
    i = sentence.count('a')
    i +=sentence.count('e')
    i +=sentence.count('i')
    i +=sentence.count('o')
    i +=sentence.count('u')
    return i
