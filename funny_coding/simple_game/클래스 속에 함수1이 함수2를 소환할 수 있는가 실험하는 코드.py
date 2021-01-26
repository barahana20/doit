class Cal:
    def __init__(self):
        pass

    def add(self, a, b):
        return a+b

    def func_add(self):
        cal2 = Cal()

        print(cal2.add(4,5))

cal1 = Cal()
cal1.func_add()