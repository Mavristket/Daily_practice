num=1234
rev=0
temp=num
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
if num==temp:
    print("number is palindrome")
else:
    print("number is not palindrome")