from product import *

class Basket():
    def __init__(self,list1):
        self.list1 = list1
        print("make new basket")
    
    def printTotalBasket(self):
        sum1 = 0
        for i in self.list1:
            sum1 = sum1 + i.amount * i.price
        print("total basket price:", sum1)
        
    def __repr__(self):
        ll = ""
        for i in self.list1:
            ll = ll + i.prType +" " + str(i.price) + " " + str(i.amount) + "\n"
        return (ll)

def testBasket():
    p1 = Product("cucumber",10,3)
    p2 = Product("milk",5,2)
    p3 = Product("yugurt",3,4)
    p = Basket([p1,p2,p3])
    print(p)
    p.printTotalBasket()

if __name__ == '__main__':
    testBasket()   
