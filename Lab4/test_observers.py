#TDD-фреймворк
import unittest
from observer import Citizen
from observer import PublisherNewspaper


class ObserverTestCase(unittest.TestCase):

    # проверка добавления нового подписчика
    def test_subscribe(self):
        person_subscriber = Citizen("Петя")
        newspaper = PublisherNewspaper()    

        newspaper.subscribe(person_subscriber)
       
        self.assertEqual(type(person_subscriber), type(newspaper.observers[0]))
        

    # проверка удаления подписчика
    def test_unsubscribe(self):
        person_subscriber = Citizen("Петя")
        newspaper = PublisherNewspaper() 
        newspaper.subscribe(person_subscriber)

        newspaper.unsubscribe(person_subscriber)

        self.assertEqual(0, len(newspaper.observers))
       

    # проверка реакции на поступление новых кроссовок людей, подписанных на кроссовки
    def test_react_sneakers_subscriber(self):
        newspaper = PublisherNewspaper() 
        person_subscriber = Citizen("Петя")
        message='Наблюдатель - поведенческий шаблон проектирования'
       
        self.assertEqual( f'Петя узнал(-а) следующее: {message}',
                         person_subscriber.update(message))


    if __name__ == '__main__':
        unittest.main()