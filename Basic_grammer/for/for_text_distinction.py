a = input()
b = input()
temp = 0

if(a == b):
    for i in range(len(a)):
        if(a[i] == b[i]):
            temp = 1
            break

if(temp == 0):
    print("str False")
else:
    print("str Ture")