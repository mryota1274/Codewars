import string

title=input()
result = title.translate(str.maketrans( '', '',string.punctuation))
result=result.replace(' ','_')
print(result+".py")
