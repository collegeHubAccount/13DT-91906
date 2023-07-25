import random

class res(object):
    def __new__(self, order) -> None:
        self.multi = 10**int(str(order)[-1])
        self.ans = int(str(order)[0:-1])*self.multi
        return int(self.ans)