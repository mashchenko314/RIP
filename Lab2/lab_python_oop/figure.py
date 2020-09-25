from abc import ABC, abstractmethod

#абстрактный класс
class Figure(ABC):
   
    # абстрактный метод, который будет необходимо переопределять для каждого подкласса
    @abstractmethod
    def square(self):
        pass