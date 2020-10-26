from lab_python_fp.cm_timer import cm_timer_1
from lab_python_fp.print_result import print_result
from lab_python_fp.unique import Unique
from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random
import json
import sys
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'data_light.json')

with open(my_file, encoding='utf-8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    return Unique(field(arg, 'job-name'), ignore_case=True)


@print_result
def f2(arg):
    return filter(lambda x: x.startswith('программист') or x.startswith('Программист'), arg)


@print_result
def f3(arg):
    print(arg)
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    salaries = gen_random(len(arg), 100000, 200000)
    res = list(zip(arg, (list(map(lambda x: ', зарплата ' + x + ' руб', ''.join(str(list(salaries)))[1:-1].split(', '))))))
    return [''.join(i) for i in res]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))