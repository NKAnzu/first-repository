from random import randrange
def get_inputs():
    return int(input('주사위 면의 갯수 입력--->'))

class FunnyDice():
    def __init__(self, n=6):
        '''
        if you create FunnyDice instance, then you can set dices'number of sides.
        n is what you set for dices'sides
        options is what you can choose with index in this class it will be randomly selected
        index is randomly selected between 1~n
        val is actual number of side by using self.option[self.index]
        '''
        self.n=n
        self.options = list(range(1,n+1))
        self.index = randrange(0, self.n)
        self.val = self.options[self.index]
    def throw(self):
        self.index = randrange(0, self.n)
        self.val = self.options[self.index]
    def getval(self):
        return self.val
    def setval(self,val):
        if val <= self.n:
            self.val=val
        else:
            msg = "주사위에 없는 숫자네요. 주사위는 1~{0}까지 있습니다!".format(self.n)
            raise ValueError(msg)

def main():
    n = get_inputs()
    mydice = FunnyDice(n)
    mydice.throw()
    print("주사위 숫자 {}".format(mydice.getval()))
    print(mydice.setval(5))
    #mydice.setval(10) #error
    print(mydice.getval())
    
if __name__ == '__main__':
    main()
