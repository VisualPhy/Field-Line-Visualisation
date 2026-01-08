import math as m
from manim import*

class mVector:
    def __init__(self, x,y,z):
        self.x_comp = x
        self.y_comp = y
        self.z_comp = z

    def get_magnitude(self):
        return m.sqrt(self.x_comp**2 + self.y_comp**2 + self.z_comp**2)
    
    def __add__(self,other):
        return mVector(self.x_comp+other.x_comp,self.y_comp+other.y_comp,self.z_comp+other.z_comp)
    
    def __sub__(self,other):
        return mVector(self.x_comp-other.x_comp,self.y_comp-other.y_comp,self.z_comp-other.z_comp)
    
    def __mul__(self, other):
        if type(other) == float:
            return mVector(other*self.x_comp, other*self.y_comp,other*self.z_comp)
        elif type(other) == mVector:
            return self.x_comp*other.x_comp + self.y_comp*other.y_comp +self.z_comp*other.z_comp
        
    def __str__(self):
        return f"[{self.x_comp},{self.y_comp},{self.z_comp}]"
    
    def get_as_point(self):
        return [self.x_comp, self.y_comp, self.z_comp]
    
    def display(self):
        l = Line([0,0,0], self.get_as_point()).add_tip(tip_length=0.2, tip_width=0.2)
        return l
    
    def normalize(self):
        mag = self.get_magnitude()
        if mag == 0:
            return self
        return self * (1 / mag)


def dist(x1,x2,y1,y2):
    return m.sqrt((x2-x1)**2 + (y2-y1)**2)
def main():
    v1 = Vector(2,0,0)
    v2 = Vector(3,1,1)
    v3 = v1-v2

    print(v3,v1.get_magnitude(), v3.get_magnitude())

if __name__ == "main":
    main()

