num=153
l=len(str(num))
pro=0
tem=num
while num>0:
  rem=num%10  #3
  pro=pro+rem**l
  num=num//10
print(pro)
if  pro==tem:
  print("armstrong")
else:
  print("non armstrong")