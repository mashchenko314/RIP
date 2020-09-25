from lab_python_oop.rectangle import Rectangle
from lab_python_oop.color import FigureColor

class Square(Rectangle): 

    figure_type = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.figure_type

    def __init__(self, color, length):
        self.length = length
        super().__init__( self.length, self.length, color)

    def __repr__(self):
        return '{} {} цвета со стороной {} площадью {}.'.format(
            Square.get_figure_type(),
            self.figurecolor.color,
            self.length,
            self.square()
        )