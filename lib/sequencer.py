from array import array
from lib.synth import Synth
import audiocore
import audiopwmio
import audiomixer
import board

class Sequence :
    def __init__(self, sample = None, lenght:int = 8, loop:bool = False) -> None:
        self.sample = sample
        self.track = [0 for _ in range(lenght)]
        self.current_spot = 0
        self.loop = loop

    def setSpot(self, spot:int, level:float=1) -> None:
        self.track[spot] = level

    def getSpot(self) -> float:
        level = self.track[self.current_spot]
        self.current_spot += 1
        if self.current_spot >= len(self.track):
            self.current_spot = 0
        return level

    def setSample(self, sample, loop:bool = False) -> None:
        self.sample = sample
        self.loop = loop

    def getSample(self):
        return self.sample

    def setLoop(self, loop:bool) -> None:
        self.loop = loop

    def getLoop(self) -> bool:
        return self.loop

class Sequencer :
    def __init__(self, voice_cnt:int = 4, sequence_len:int = 8) -> None:
        self.synth = Synth(voice_cnt)
        self.sequences = [Sequence(lenght=sequence_len) for _ in range(voice_cnt)]

    def setSequenceSample(self, sequence:int, sample, loop:bool = False) -> None:
        self.sequences[sequence].setSample(sample, loop)

    def getSequence(self, sequence:int) -> Sequence:
        return self.sequences[sequence]

    def playStep(self) -> None:
        for i, sequence in enumerate(self.sequences) :
            self.synth.play_sample(sequence.getSample(), sequence.getSpot(), sequence.getLoop(), i)