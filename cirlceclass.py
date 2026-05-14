class circle:
    pai = 3.14
    def __init__(self,radius):
        self.radius = radius
        
    def circle_circumference(self):
        formula_circumference = 2*circle.pai*circle.radius
        return formula_circumference
    def circle_area(self):
        formula_area = circle.pai*self.radius**2
        return formula_area
    
c1 = circle(23)
c2 = circle(25)
print(c2.circle_area())

        