

class Product():
    def __init__(self,prType,price, amount):
        self.prType = prType
        self.price = price
        self.amount = amount
    
    def printProduct(self):
        print(self.prType, self.price, self.amount)
        
    def __repr__(self):
        return ("{0} {1} {2}".format(self.prType , self.price, self.amount)  )

def testProcut():
    p = Product("shoes",350,1)
    p.printProduct()
    print(p)

if __name__ == '__main__':
    testProcut()   
