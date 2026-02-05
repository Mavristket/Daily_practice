def pal(num,rev=0):
    if num==0:
        return rev
    return pal(num//10,rev*10+num%10)