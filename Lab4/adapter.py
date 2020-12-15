# структурный паттерн проектирования
# адаптер
# предметная область: преобразует один интерфейс в другой, позволяя совместить квадратные колышки и круглые отверстия
#                     Адаптер вычисляет наименьший радиус окружности, в которую можно вписать квадратный колышек, 
#                     и представляет его как круглый колышек с этим радиусом.

#Адаптируемый класс
class RoundPeg:

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius


#Адаптируемый класс
class SquarePeg:

    def __init__(self, width):
        self.width = width

    def get_width(self):
        return self.width

#Целевой класс объявляет интерфейс, с которым может работать клиентский код
class RoundHole:

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def fits(self, round_peg):

        if self.get_radius() >= round_peg.get_radius():
            return f"Деталь подходит. " \
                   f"Радиус детали: {round_peg.get_radius()}, радиус отверстия {self.get_radius()}"
        else:
            return f"Деталь не подходит. " \
                   f"Радиус детали: {round_peg.get_radius()}, радиус отверстия {self.get_radius()}"



#Адаптер позволяет использовать квадратные колышки и круглые
#отверстия вместе.
class SquarePegAdapter (RoundPeg):
    
    def __init__(self, square_peg):
        self.square_peg = square_peg

    def get_radius(self):
        return self.square_peg.get_width() / 2


def client_code():
   hole = RoundHole(5)
   rpeg = RoundPeg(5)
   print(hole.fits(rpeg) )

   small_sqpeg = SquarePeg(5)
   large_sqpeg = SquarePeg(12)
   #hole.fits(small_sqpeg) 

   small_sqpeg_adapter = SquarePegAdapter(small_sqpeg)
   large_sqpeg_adapter = SquarePegAdapter(large_sqpeg)
   print(hole.fits(small_sqpeg_adapter))
   print(hole.fits(large_sqpeg_adapter))


if __name__ == "__main__":
    client_code()