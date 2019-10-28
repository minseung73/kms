def add(a, b):
    c = a + b
    return c

def sub(a, b):
    c = a - b
    return c

def mul(a, b):
    c = a * b
    return c

def div(a, b):
    c = a / b
    return c

c = int(input())
while(True):
    temp = int(input())
    temp_2 = int(input())

    if(c == 1):
        print(add(temp, temp_2))
    elif(c == 2):
        a = (sub(temp, temp_2))
        print(a)
    elif(c == 3):
        print(mul(temp, temp_2))
    elif(c == 4):
        b = (div(temp, temp_2))
        print(b)