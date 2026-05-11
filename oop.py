class product:
    def __init__(self,product_name,brand_name,model_name,price):
        self.product_name = product_name
        self.brand_name = brand_name
        self.model_name = model_name 
        self.model_price = price
        self.productnamewithmodelname= product_name + '' + str(model_name)

shoes = product('shoes', 'nike', 'inifinity' , 10000)
mobile = product('Mobile', 'apple', 'iphone - 14' , 80000)
print(shoes.brand_name)
print(mobile.model_price)
print(mobile.productnamewithmodelname)