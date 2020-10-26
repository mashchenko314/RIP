import time
from contextlib import contextmanager


class cm_timer_1:

    def __init__(self):
        self.start_time = time.time()

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type is not None:
            print(exc_type, exc_val, traceback)
        else:
            print('time: ', time.time() - self.start_time)


@contextmanager
def cm_timer_2():
    start_time = time.time()
    yield 333
    print('time: ', time.time() - start_time)


def main():
    with cm_timer_1():
        time.sleep(5.5)

    with cm_timer_2():
        time.sleep(2.5)


if __name__ == '__main__':
    main()