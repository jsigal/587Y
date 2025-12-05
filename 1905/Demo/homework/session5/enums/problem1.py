# Problem 1: Traffic Light Simulation
# •	Create an Enum: Define an Enum called LightColor with members RED, YELLOW, and GREEN.
# •	Create a Class: Define a class TrafficLight.
# o	It should have an instance attribute current_color initialized to LightColor.RED.
# o	Implement a method change_light() that cycles the current_color from RED to GREEN, then GREEN to YELLOW, and YELLOW back to RED.
# o	Implement a method get_status() that returns a string indicating the current light color, e.g., "The traffic light is currently RED."

from enum import Enum


class LightColor(Enum):
    RED = "RED"
    YELLOW = "YELLOW"
    GREEN = "GREEN"


class TrafficLight:
    def __init__(self):
        self.current_color = LightColor.RED
    
    def change_light(self):
        """Cycles the traffic light: RED -> GREEN -> YELLOW -> RED"""
        if self.current_color == LightColor.RED:
            self.current_color = LightColor.GREEN
        elif self.current_color == LightColor.GREEN:
            self.current_color = LightColor.YELLOW
        elif self.current_color == LightColor.YELLOW:
            self.current_color = LightColor.RED
    
    def get_status(self):
        """Returns a string indicating the current light color"""
        return f"The traffic light is currently {self.current_color.value}."

tl = TrafficLight()
print(tl.get_status())
tl.change_light()
print(tl.get_status())
tl.change_light()
print(tl.get_status())
tl.change_light()
print(tl.get_status())
tl.change_light()
print(tl.get_status())
