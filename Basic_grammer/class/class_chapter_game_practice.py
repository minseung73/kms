import random

class Chapter:

    def __init__(self):

        self.sex = random.randrange(0, 2)#0이면 남자 1이면 여자
        self.hp = random.randrange(10, 20)
        self.mp = random.randrange(20, 30)
        self.atk = random.randrange(1, 3)

    def attacked(self, atk):

        self.hp = self.hp - atk

    def attack(self):

        return self.atk

chapter_user = Chapter()
chapter_com = Chapter()
print("user의 기본체력", chapter_user.hp)
print("com의 기본체력", chapter_com.hp)
turn = "user"

while(True):
    import random
    b = random.randrange(1,2)

    if(turn == "user"):
        a = int(input())
        if(a == 1):
            print("turn-user")
            chapter_com.attacked(chapter_user.atk)
            print("user의 남은체력", chapter_user.hp)
            print("com의 남은체력", chapter_com.hp)
            turn = "com"
    else:
        print("turn-com")
        chapter_user.attacked(chapter_com.atk)
        print("user의 남은체력", chapter_user.hp)
        print("com의 남은체력", chapter_com.hp)
        turn = "user"