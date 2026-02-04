def call_by_value(x):
    x=x*5
    return x
def call_by_ref(a):
    a.append(10)
    return a
num=5
a=[10]
value=0
ref=[]
value=call_by_value(num)
ref=call_by_ref(a)

print(value)
print(ref)