from lab_python_fp.gen_random import gen_random

class Unique(object):
    """Итератор, оставляющий только уникальные значения."""
    def __init__(self, items, **kwargs):
        self.used_elements = set() 
        self.items = items
        self.index = 0
        if len(kwargs)!=0:
            self.ignore_case=kwargs
        else:
            self.ignore_case=False

    def __iter__(self):
        return self

    def __next__(self):
        while True:
                for item in self.items:
                    current = item     
                    self.index = self.index + 1
                    if (current not in self.used_elements)\
                        and not(self.ignore_case and current.swapcase() in self.used_elements):
                        self.used_elements.add(current)
                        return current
                else:
                    raise StopIteration


def main():
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print(data1)
    itr1 = Unique(data1)
    for i1 in itr1:
        print(i1, end=' ')
    print('\n', end='')
    data2 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(data2)
    itr2 = Unique(data2)
    for i2 in itr2:
        print(i2, end=' ')
    print('\n', end='')
    print(data2)
    itr3 = Unique(data2, ignor_case=True)
    for i3 in itr3:
        print(i3, end=' ')
    print('\n', end='')
    data3 = gen_random(5, 1, 3)
    itr4 = Unique(data3)
    for i4 in itr4:
        print(i4, end=' ')


if __name__ == "__main__":
    main()
