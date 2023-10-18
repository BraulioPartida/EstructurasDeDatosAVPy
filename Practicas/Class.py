class ojo:
    def __init__(self):
        self.i = 8

    def f1(self, y=2):
        return self.i + y


d = ojo()
print(d.f1())
print(d.f1(9))
