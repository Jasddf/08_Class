#연습문제4
class Login:
    def __init__(self,name,age,number):
        self.User_name = name
        self.User_age = age
        self.User_number = number
    def 입력(self):
        print('입력하신 이름은',self.User_name,'이며, 나이는',self.User_age,'그리고 연락처는',self.User_number,'입니다.')

My_Login = Login('장영수','29살','010-8711-9415')
My_Login.입력()
