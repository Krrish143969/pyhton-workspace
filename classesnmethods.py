class product:
    def __init__(self,productname,price):
        self.proctname = productname
        self.price = price
    def discount(self,discountvalue):
        discountamount = (self.price/100)*discountvalue
        final_price = self.price - discountamount
        return int(final_price)


laptop = product('laptop',55000)
mobile = product('mobile', 40000)
print(laptop.discount(25))
print(mobile.price)
print(mobile.discount(10))

