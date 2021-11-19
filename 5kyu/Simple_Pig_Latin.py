def pig_it(text):
    #your code here
    newWord = ""
    for word in text.split(" "):
        if word.isalpha():
            newWord += word[1:] + word[0] + "ay "
        else:
            newWord += word
    
    return newWord.rstrip()
