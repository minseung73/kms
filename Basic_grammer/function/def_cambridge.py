def distinction(a, b):
    for i in range(len(a)):
        flag = 0
        for u in range(len(b)):
            if (a[i] == b[u]):
                flag = 1

        if (flag == 0):
            check_list.append(a[i])

a = input()
b = ["C", "A", "M", "B", "R", "I", "D", "G", "E"]

check_list = []

distinction(a, b)

print(check_list)