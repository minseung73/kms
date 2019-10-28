import random

temp_rist = []
for i in range(10):
    i = random.randrange(1, 100)
    temp_rist.append(i)
print(temp_rist)

prime_list = []
for u in range(len(temp_rist)):
    value = temp_rist[u]
    flag = 0

    for j in range(2, value):
        if (value % j == 0):
            flag = 1
    if (flag == 0):
        prime_list.append(value)
print(prime_list)