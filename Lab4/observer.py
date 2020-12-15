# поведенческий паттерн проектирования
# наблюдатель
# предметная область: новостная газета делает рассылку подписчикам, при публикации очередной новости

from abc import ABC, abstractmethod

class Observer(ABC): 
    # Общий интерфейс подписчиков

    @abstractmethod
    def update(self, message: str) -> None:

        pass


class EventManager(ABC):
    #базовый класс-издатель
    def __init__(self) -> None:
        self.observers = []     # инициализация списка наблюдателей

    def subscribe(self, observer: Observer) -> None:
       #Регистрация нового наблюдателя на подписку
        print (observer.name + " подписался(-ась) на новостные обновления")
        self.observers.append(observer)
    
    def unsubscribe(self, observer):
        print (observer.name + " отписался(-ась) от новостных обновлений")
        self.observers.remove(observer)

    def notify(self, message: str) -> None:
        #Передача сообщения всем наблюдателям, подписанным на газету
       
        for observer in self.observers:
            print(observer.update(message))

class PublisherNewspaper(EventManager):
    #Конкретный класс-издатель, в данном случае новостная газета, в которую добавляются новости

    def add_news(self, news: str) -> None:
        #Выпуск очередной новости

        self.notify(news)


class Citizen(Observer):
    #Конкретный подписчик -гражданин, который хочет подписаться на новости

    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, message: str):
        #Получение очередной новости
        return f'{self.name} узнал(-а) следующее: {message}'

def client_code():
    newspaper = PublisherNewspaper()                 # создаем небольшую газету
    person_one=Citizen('Елена')
    person_two=Citizen('Максим')
    newspaper.subscribe(person_one)     # добавляем двух человек, которые
    newspaper.subscribe(person_two)  # ... ее регулярно выписывают
    # ... и публикуем очередную новость
    newspaper.add_news('Наблюдатель - поведенческий шаблон проектирования')
    #отписываем от обновлений первого человека
    newspaper.unsubscribe(person_one)


if __name__ == '__main__':
    client_code()
