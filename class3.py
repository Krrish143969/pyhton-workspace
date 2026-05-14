class laptop:
    discount = 10
    sno = 0
    def __init__(self,name,price):
        laptop.sno += 1
        self.sno = laptop.sno
        self.name = name
        self.price = price
    def applydiscount(self):
        discount_amount = self.price/100*self.discount
        finalamount = self.price - discount_amount
        return finalamount

m6600 = laptop('m6600', 55000)
m4800 = laptop('m4800', 55000)
m7700 = laptop('m7700',55000)
m6700 = laptop('m6700',55000)
m7700.discount = 3
m6700.discount = 0
m4800.bluetooth = 'yes'
m4800.discount = 5
print(m6600.applydiscount())
print(m4800.applydiscount())
print(m7700.applydiscount())
print(m6700.applydiscount())
print(m6600.__dict__)
print(m4800.__dict__)
print(m7700.__dict__)
print(m6700.__dict__)

