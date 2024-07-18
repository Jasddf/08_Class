#연습문제3
class House:
    def __init__(self,위치,평수,건물종류,가격,준공년도):
        self.H_위치 = 위치
        self.H_평수 = 평수
        self.H_건물종류 = 건물종류
        self.H_가격 = 가격
        self.H_준공년도 = 준공년도
    def check(self):
        print('해당 집의 정보는', self.H_위치,self.H_평수,self.H_건물종류,self.H_가격,self.H_준공년도, '입니다.')

my_House = House('용인','34평','아파트','5억','1999년')
my_House.check()
