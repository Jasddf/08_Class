#연습문제1
class 사칙연산:
    def add (self,a,b):
        result = a+b
        return result
    def mul (self,a,b):
        result = a*b
        return result

app = 사칙연산()
print(app.add(3,4))
print(app.mul(3,4))

