class student:
    total_marks = 1000
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
        self.total_marks = student.total_marks

    

s1 = student('krrish' , 20, 890)
s2 = student('arin' , 20, 763)
s3 = student('piyush' , 19, 699)
s4 = student('anubhav' , 22, 345)
s5 = student('adu' , 19, 240)
print(s1.total_marks) 

