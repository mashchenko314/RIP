from unittest import TestCase
from unittest.mock import patch
from factory_method import WindowsDialogCreator
from factory_method import WebDialogCreator


class FactoryMethodTestCase(TestCase):

    # проверяем работу метода render Создателя для WindowsButton
    @patch('factory_method.get_event', return_value="closeDialog")
    def test_win_button(self, get_event):
        creator=WindowsDialogCreator()
        self.assertEqual("Вешаем на кнопку обработчик событий Windows:closeDialog\nОтрисовка кнопки в стиле Windows.",
                         creator.render(get_event()))

   # проверяем работу метода render Создателя для HTMLButton
    @patch('factory_method.get_event', return_value="closeDialog")
    def test_html_button(self, get_event):
        creator=WebDialogCreator()
        self.assertEqual("Вешаем на кнопку обработчик события браузера:closeDialog\nВозвращаем HTML-код кнопки.",
                         creator.render(get_event()))