a = {6,7,8,9,10}
b ={5,6,7,8,9}
a.add(4)
print(a)
b.add(3)
print(b)
d=a.union(b)
print(d)
e=b.union(a)
print(e)
x=a.difference(b)
print(x)
y=b.difference(a)
print(y)
t=a.intersection(b)
print(t)
r=b.intersection(a)
print(r)

lst = [11, 100, 99, 1000, 999, 99]
print(lst[0])
print(lst[5])
nbr=0
print(max(lst))
print(min(lst))

yeays=range(2020,2070)
for a in yeays:
    if a%10==0:
        print(a)
r=range(1000,2000)
for a in r:
    if a%7==0:
        print(a)
        if a%5!=0:
            print(a)
t=range(11)
for a in t:
    print(t)
w=range(30,50)
for d in w:
  if d%2==0:
   print (d)



