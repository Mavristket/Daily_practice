num=1221 #1
rev=0
tem=num
while num>0:
  rem=num%10  #1
  rev=rev*10+rem
  num=num//10
if rev==tem:
  print("palindrome number")
else:
  print("non palindrome")