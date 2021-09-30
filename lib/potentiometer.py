import board
from analogio import AnalogIn

class Potentiometer:
    def __init__(self, pin) -> None:
        self.potentiometer = AnalogIn(pin)
        self.last_position = None

        self.new_position = False

    def read(self) -> None:
        position = round(self.potentiometer.value/65536.0, 2)
        if self.last_position is None or position != self.last_position:
            self.new_position = True
        self.last_position = position

    def isNewPosition(self) -> bool:
        return self.new_position

    def getPosition(self) -> int:
        self.new_position = False
        return round(self.potentiometer.value/65536.0, 2)