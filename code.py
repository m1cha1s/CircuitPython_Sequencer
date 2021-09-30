from lib.sequencer import Sequence, Sequencer
from lib.potentiometer import Potentiometer
from lib.encoder import Encoder
from analogio import AnalogIn
from lib.synth import Synth
import board, time
import audiocore

enc = Encoder(board.GP13, board.GP12)
pot = Potentiometer(board.A2)

seq = Sequencer()

seq.setSequenceSample(0, audiocore.WaveFile(open("samples/kick.wav", "rb")))
seq.setSequenceSample(1, audiocore.WaveFile(open("samples/snare.wav", "rb")))
seq.setSequenceSample(2, audiocore.WaveFile(open("samples/dbass.wav", "rb")), True)

seq.getSequence(0).setSpot(0)
seq.getSequence(0).setSpot(2)
seq.getSequence(0).setSpot(4)
seq.getSequence(0).setSpot(6)

seq.getSequence(1).setSpot(1, 0.1)
seq.getSequence(1).setSpot(3, 0.1)
seq.getSequence(1).setSpot(5, 0.1)
seq.getSequence(1).setSpot(6, 0.1)
seq.getSequence(1).setSpot(7, 0.1)

seq.getSequence(2).setSpot(1, 1)
seq.getSequence(2).setSpot(2, 0.5)
# seq.getSequence(2).setSpot(3, 0.6)
seq.getSequence(2).setSpot(5, 1)
seq.getSequence(2).setSpot(6, 0.5)



while True :
    seq.playStep()
    time.sleep(pot.getPosition())
