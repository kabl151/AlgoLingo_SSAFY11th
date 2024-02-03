# 아래 클래스를 수정하시오.
class Shape:
    def print_info(self, a, b):
        self.a = a
        self.b = b
        print(f'Width: {self.a}')
        print(f'Height: {self.b}')
        print(f'Area: {2 * (self.a + self.b)}')
        print(f'Perimeter: {self.a * self.b}')

shape1 = Shape(5, 3)
shape1.print_info()
