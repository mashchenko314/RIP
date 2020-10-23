# используется для сортировки
from operator import itemgetter

class Lang:
    """Язык программирования"""
    def __init__(self, id, name, rating, tool_id):
        self.id = id
        self.name = name
        self.rating = rating
        self.tool_id = tool_id

class DevTool:
    """Средство разработки"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class LangDevTool:
    """
    'Средства разработки языков программирования' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, lang_id, tool_id):
        self.lang_id = lang_id
        self.tool_id = tool_id

# Средства разработки
devTools = [
    DevTool(1, 'Android Studio'),
    DevTool(2, 'IntelliJ IDEA'),
    DevTool(3, 'Visual Studio Code 2020'),
    DevTool(4, 'Visual Studio 2019'),
    DevTool(13, 'CLion'),
    DevTool(20, 'PyCharm'),
]

# Языки программирования
langs = [
    Lang(1, 'Java', 95.3, 1),
    Lang(2, 'JavaScript', 79.5, 3),
    Lang(5, 'C++', 87, 4),
    Lang(11, 'C#', 48.1, 4),
    Lang(19, 'Python', 100, 20),
    Lang(31, 'F#', 34.7, 4),
]

langs_devTools = [
    LangDevTool(1,1),
    LangDevTool(1,2),
    LangDevTool(2,3),
    LangDevTool(5,4),
    LangDevTool(5,13),
    LangDevTool(11,4),
    LangDevTool(19,3),
    LangDevTool(19,4),
    LangDevTool(19,20),
    LangDevTool(31,4),
]

def main():
    """Основная функция"""

    # Соединение данных один-ко-многим 
    one_to_many = [(l.name, l.rating, t.name) 
        for l in langs 
        for t in devTools 
        if l.tool_id==t.id]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(t.name, ldt.lang_id, ldt.tool_id) 
        for t in devTools 
        for ldt in langs_devTools 
        if t.id==ldt.tool_id]
   
    many_to_many = [(l.name, l.rating, tool_name) 
        for tool_name, lang_id, tool_id in many_to_many_temp
        for l in langs
        if l.id==lang_id]
   

    print('Задание D1')
    res1 = []
    for i in one_to_many:
        if i[0].endswith('#') ==True:
            res1.append(i[0:3:2])
    print(res1)
    
    print('\nЗадание D2')
    res_12_unsorted = []
    # Перебираем все средства разработки(инструменты)
    for t in devTools:
        # Список языков, поддерживаемых инструментом разработки
        t_langs = list(filter(lambda i: i[2]==t.name, one_to_many))       
        if len(t_langs) > 0:
            # Находим средний рейтинг языков для каждого инструмента
            t_rating = [rating for _,rating,_ in t_langs]
            t_rating_sum = sum(t_rating)
            t_rating_count = len(t_rating)
            t_rating_average = t_rating_sum / t_rating_count
            res_12_unsorted.append((t.name, t_rating_average))

    # Сортировка по среднему рейтингу
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание Д3')
    res3 = {}
    # Перебираем все средства разработки(инструменты)
    for t in devTools:
        #Выбираем инструменты, название которых начинается на букву V
        if t.name[0] == "V":
            t_langs = list(filter(lambda i: i[2] == t.name, many_to_many))
            # Только название языка
            o_langs_names = [x for x, _, _ in t_langs]
            # Добавляем результат в словарь
            # ключ - инструмент, значение - список языков
            res3[t.name] = o_langs_names
    print(res3)

  
if __name__ == '__main__':
    main()
