class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def result(self):
        if self.marks >= 500:
            return 'pass'
        else:
            return 'fail'


s1 = student('Krrish',589)
s2 = student('Piyush', 533)
s3 = student('Anubhav',333)
s4 = student('Arin',555)
s5 = student('Dhaiya',435)
student_objects = [s1,s2,s3,s4,s5]
passstudents = []
failstudents = []
student_result = {}
for x in student_objects:
    if x.result() == 'pass':
        passstudents.append(x.name)
        student_result['pass students '] = passstudents
    else:
        failstudents.append(x.name)
        student_result['failed students '] = failstudents
print (student_result)

         