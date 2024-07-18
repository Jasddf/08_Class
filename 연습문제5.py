#연습문제5
class Messages:
    def __init__(self,l,p1,p2):
        self.len = l
        self.pay1 = p1
        self.pay2 = p2

    def 문자요금(self,text):
        print(text)
        if len(text) <= self.len :
            print(self.pay1)
        elif len(text) > self.len :
            print(self.pay2)

My_Messages = Messages(30,100,200)
My_Messages.문자요금('dddd')