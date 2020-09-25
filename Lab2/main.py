from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

def main():
    r = Rectangle( 11, 11, "синего")
    c = Circle("зеленого", 11)
    s = Square("красного", 11)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    # execute only if run as a script
    main()