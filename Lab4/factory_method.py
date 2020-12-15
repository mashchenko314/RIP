# порождающий паттерн проектирования
# фабричный метод
# предметная область: создание кросс-платформенных элементов интерфейса без привязывания основного кода программы к конкретным классам элементов

from abc import ABC, abstractmethod

def get_event():
    return "closeDialog"

class Button(ABC):
    """
    Интерфейс Button объявляет операции, которые должны выполнять все
    конкретные Button.
    """

    @abstractmethod
    def render(self):
        pass
    @abstractmethod
    def onClick(self):
        pass


"""
Конкретные реализации интерфейса Button.
"""

class WindowsButton(Button):
    def render(self):
        return "Отрисовка кнопки в стиле Windows."
    def onClick(self,f):
        return "Вешаем на кнопку обработчик событий Windows:"+f


class HTMLButton(Button):
    def render(self):
        return "Возвращаем HTML-код кнопки."
    def onClick(self,f):
        return "Вешаем на кнопку обработчик события браузера:"+f


class DialogCreator(ABC):
    """
    Класс Создатель объявляет фабричный метод, который должен возвращать объект
    класса Button. 
    """

    #фабричный метод
    @abstractmethod
    def createButton(self):
        pass


    def render(self, event):
        """
        Создатель содержит некоторую базовую бизнес-логику, которая основана на объектах,
        возвращаемых фабричным методом. 
        """

        # Вызываем фабричный метод, чтобы получить объект-кнопку.
        okButton = self.createButton()

        # Далее, работаем с этим продуктом.
        return  okButton.onClick(event) +"\n" + okButton.render()



"""
Конкретные Создатели переопределяют фабричный метод для того, чтобы изменить тип
результирующего объекта.
"""
class WindowsDialogCreator(DialogCreator):
    """
    Сигнатура метода по-прежнему использует тип
    абстрактного продукта, хотя фактически из метода возвращается конкретный
    продукт. Таким образом, Создатель может оставаться независимым от конкретных
    классов продуктов.
    """
    def createButton(self) -> Button:
        return WindowsButton()


class WebDialogCreator(DialogCreator):
    def createButton(self) -> Button:
        return HTMLButton()


def client_code(dialog: DialogCreator) -> None:
   print(dialog.render(get_event())) 


if __name__ == "__main__":
    print("App: Launched with the WindowsDialogCreator.")
    client_code(WindowsDialogCreator())
    print("\n")
    print("App: Launched with the WebDialogCreator.")
    client_code(WebDialogCreator())