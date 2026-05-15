class phone:                                  #parent class
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = max(price,0)

    def make_a_call(self, phone_num):
        print(f"calling {phone_num}....")
        
    def full_name(self):
        return f"{self.brand} {self.model_name}"
    
class smartphone(phone):                           #child class
    def __init__(self,brand,model_name,price,ram,internal_memory,rare_camera):
       
        super().__init__(brand,model_name,price)
#        phone.__init__(self,brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rare_camera = rare_camera


class smartphone2(phone):                           #child class
    def __init__(self,brand,model_name,price,ram,internal_memory,rare_camera,):
       
        super().__init__(brand,model_name,price)
#        phone.__init__(self,brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rare_camera = rare_camera


class flagship(smartphone):                           #child class
    def __init__(self,brand,model_name,price,ram,internal_memory,rare_camera,front_camera):
       
        super().__init__(brand,model_name,price,ram,internal_memory,rare_camera)
        self.front_camera = front_camera

phone1 = phone('nokia','1600',4000)
smartphone1 = smartphone('samsung','A7',60000,'4GB','128GB','25MP')
oneplus = flagship('oneplus','A-2',60000,'4GB','128GB','25MP','12MP')
print(isinstance(oneplus,flagship))




