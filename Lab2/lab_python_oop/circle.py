from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor
import math


class Circle(Figure):
   
    figure_type = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.figure_type

    def __init__(self, color, radius):
        self.radius = radius
        self.figurecolor = FigureColor()
        self.figurecolor.color = color

    def square(self):
        return math.pi*(self.radius**2)

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {}.'.format(
            Circle.get_figure_type(),
            self.figurecolor.color,
            self.radius,
            self.square()
        )