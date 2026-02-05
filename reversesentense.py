s="this is balaji"
lst=s.split()
result=[]
for word in lst:
    result.append(word[::-1])
print(" ".join(result))