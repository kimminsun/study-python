class FourCal:
    def setdata(self,first,second):
        self.first=first
        self.second=second

    def sum(self):
        result=self.first+self.second
        return print(result)

    def mul(self):
        result=self.first*self.second
        return print(result)

    def sub(self):
        result=self.first-self.second
        return print(result)

    def div(self):
        result=self.first/self.second
        return print(result)


a=FourCal()
b=FourCal()
a.setdata(4,2)
b.setdata(5,8)

a.sum()
a.mul()
a.sub()
a.div()

b.sum()
b.mul()
b.sub()
b.div()
