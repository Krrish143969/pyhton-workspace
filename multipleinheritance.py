class A:
    def class_a_method(self):
        return 'i am just a class A method'
    
    def helo(self):
        return 'hello from class A' 
    
class B:
    def class_b_method(self):
        return 'i am just a class B method'
    
    def helo(self):
        return 'hello from class B' 
    
class C(B,A):
    pass

instanceA = A()    
instanceB = B()
instanceC = C()
print(C.mro())