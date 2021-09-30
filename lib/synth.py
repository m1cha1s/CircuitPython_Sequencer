import audiocore
import audiopwmio
import audiomixer
import board


class Synth:
    def __init__(self, voice_cnt:int = 4) -> None :
        self.dac = audiopwmio.PWMAudioOut(board.GP22)

        self.mix = audiomixer.Mixer(voice_count=voice_cnt, channel_count=1, sample_rate=16000, samples_signed=True)
        
        self.dac.play(self.mix)

    def play_sample(self, sample, level:float = 0.5, loop:bool = False, voice:int = 0) -> None :
        if loop and self.mix.voice[voice].playing :
            self.mix.voice[voice].level = level
        else :
            if (sample != None or level != 0) :
                self.mix.voice[voice].play(sample, loop=loop)
            elif loop:
                self.mix.voice[voice].stop()

    def stop(self) :
        self.dac.stop()