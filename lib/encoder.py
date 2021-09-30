import board, rotaryio

class Encoder:
    def __init__(self, pin_A, pin_B) -> None:
        self.encoder = rotaryio.IncrementalEncoder(pin_A, pin_B)
        self.last_position = None

        self.new_position = False

    def read(self) -> None:
        position = self.encoder.position
        if self.last_position is None or position != self.last_position:
            self.new_position = True
        self.last_position = position

    def isNewPosition(self) -> bool:
        return self.new_position

    def getPosition(self) -> int:
        self.new_position = False
        return self.encoder.position