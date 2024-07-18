#연습문제2
class Character:
    def __init__(self,id,sex,job):
        self.Char_id = id
        self.Char_sex = sex
        self.Char_job = job
    def 기본공격(self,Mon_name):
        print(self.Char_id, '(이)가', Mon_name, '을 공격했다!')

my_Char = Character('장비','남','검사')
my_Char.기본공격('슬라임')