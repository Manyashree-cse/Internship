class StudentResult:
    def __init__(self):
        self.__score=0

    def update_score(self, new_score):
        if new_score>self.__score:
            self.__score=new_score
            print(f"Score updated to {self.__score}")
        else:
            print(f"New score is lower. Score remains: {self.__score}")

s = StudentResult()
s.update_score(70)
s.update_score(69)
s.update_score(80)