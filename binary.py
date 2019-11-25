num = int(input())
num_list = []
number_list = []
temp = int(num / 2)

num_list.append(num % 2)

while True:

    if temp == 1:
        num_list.append(temp)
        break

    num_list.append(temp % 2)
    temp = temp//2

for i in range(len(num_list)):
    number_list.append(num_list[i-1])

print(number_list)