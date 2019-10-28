#최대공약수
a = int(input())
b = int(input())
temp_a = a
c = 0

if(a > b):
    temp_a = b

    for i in range(1, b+1):
        if(b % i == 0 and a % i == 0):
            c = i
print(c)