# COLOR_RED = 1
# COLOR_GREEN = 2
# COLOR_BLUE = 3

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class ColorChanger:
    def __init__(self):
        self._color = Color.RED
    @property
    def color(self) ->Color: # pylint: disable=C0116
        return self._color
    @color.setter
    def color(self, newcolor: Color):
        if newcolor.value not in {m.value for m in Color}:
            raise ValueError(f"{newcolor.value} is not a valid color")
        dict_color = {m.value:m.name for m in Color}
        print(dict_color)
        self._color = newcolor

c = ColorChanger()
c.color = Color.GREEN
print(c.color)
# c.color = 255
# print(c.color)