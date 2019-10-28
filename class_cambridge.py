class full_frame:

    def __init__(self):

        self.cambridge = ["C", "A", "M", "B", "R", "I", "D", "G", "E"]

    def distinction(self, a):
        for i in range(len(a)):
            flag = 0
            for u in range(len(self.cambridge)):
                if (a[i] == self.cambridge[u]):
                    flag = 1

            if (flag == 0):
                check_list.append(a[i])

a = input()

check_list = []

temp_full_frame = full_frame()

temp_full_frame.distinction(a)

print(check_list)
