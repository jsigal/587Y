COLOR_RED = 1
COLOR_GREEN = 2
COLOR_BLUE = 3

class ColorChanger:
    def __init__(self):
        self._color = COLOR_RED
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, value: int):
        self._color = value

c = ColorChanger()
c.color = COLOR_GREEN
print(c.color)
c.color = 255
print(c.color)