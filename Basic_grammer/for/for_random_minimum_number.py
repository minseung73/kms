import random

a = []
for i in range(10):
    i = random.randrange(1, 100)
    a.append(i)
print(a)

b = a[0]
for u in range(len(a)):
    if(b > a[u]):
        b = a[u]

print("minimum", b)