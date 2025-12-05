from enum import Enum

class TrafficLightColor(Enum):
    RED = "Stop"
    YELLOW = "Prepare to Stop"
    GREEN = "Go"

class TrafficLight:
    def __init__(self, color):
        self.color = color

    def display_message(self):
        print(f"The traffic light shows: {self.color.value}")

# Example usage
traffic_light = TrafficLight(TrafficLightColor.RED)
traffic_light.display_message()