#클래스(함수 이름은 대문자로 작성, 변수 이름은 소문자로 작성)
class Dog:
    def __init__(self,name,breed,sex):
        self.dog_name = name
        self.dog_breed = breed
        self.dog_sex = sex
    def bark(self):
        print(self.dog_name + '가 짖습니다!')

my_dog = Dog('누니','말티즈','남')
my_dog.bark()

