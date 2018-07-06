class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self): # = toString()
        return f"({self.x},{self.y})"

class Rectangle: # ni public, ni private
    # constructeur
    def __init__(self, width, height, origin): # self = this obligaoire
        self.width = width
        self.height = height #pas de déclarations de variables de classe, ni getter/setter quand pas private
        self.origin = origin

    def surface(self):
        return self.width * self.height # self est toujour obligatoire (contrairement à this in Java)


class Carre(Rectangle): #means 'Carre hérite rectangle'
    def __init__(self, cote, origin):
        super().__init__(cote, cote, origin)


if __name__ == '__main__':
    p1 = Point(2, -1)
    r1 = Rectangle(2,3, Point(2, -1)) # pas de new ni class devant la variable
    print(r1.surface())

    c1 = Carre(2, p1)
    print(c1.surface())

    r1 = c1
    r1.origin = p1
    print(p1.__repr__())
