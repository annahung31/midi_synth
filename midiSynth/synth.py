import numpy as np
from scipy.io.wavfile import write
import pretty_midi
from IPython.display import Audio
from IPython.core.display import display

class MidiSynth(object):
    def __init__(self, path_sf=None):
        self.path_sf = path_sf
        
    def play_midi(self, path_midi):
        a_1 = self._read_midi(path_midi)
        display(Audio(a_1, rate=44100))
    
    def _read_midi(self, path_midi):
        midi_data = pretty_midi.PrettyMIDI(path_midi)
        a_1 = midi_data.fluidsynth(sf2_path=self.path_sf)
        return a_1
    
    def midi2audio(self, path_midi, path_out='output.mp3'):
        a_1 = self._read_midi(path_midi)
        write(path_out, 44100, a_1)  
        