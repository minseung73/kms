def start_mark():

    mark = input()

    if(mark == "X"):
        return ["X", "O"]

    elif(mark == "O"):
        return ["O", "X"]


print(start_mark())

'''
함수를 이용하여 리스트도 사용해서 게임판 만들기 3*3 
'''