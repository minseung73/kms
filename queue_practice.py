def enqueue(num):

    if(len(queue_list) == max):
        print("overflow")
    else:
        queue_list.append(num)


def dnqueue(temp_list):

    if(len(temp_list) == 0):
        print("underflow")

    elif(len(temp_list) != 0):
        print(temp_list[0])
        del (temp_list[0])
        print(queue_list)


max = 3
queue_list = []
while(True):

    temp = input()

    if(temp == "en"):
        temp_enqueue = int(input())
        enqueue(temp_enqueue)
        print(queue_list)

    elif(temp == "dn"):
        dnqueue(queue_list)

