from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor

class Rectangle(Figure): 

    figure_type = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.figure_type

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.figurecolor = FigureColor()
        self.figurecolor.color = color

    def square(self):
        return self.width*self.height

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} площадью {}.'.format(
            Rectangle.get_figure_type(),
            self.figurecolor.color,
            self.width,
            self.height,
            self.square()
        )
