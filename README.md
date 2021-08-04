# midi_synth
Display midi in jupyter notebook with good sound


## Get soundfont file

```
wget https://freepats.zenvoid.org/Piano/SalamanderGrandPiano/SalamanderGrandPiano-SF2-V3+20200602.tar.xz
tar Jxvf SalamanderGrandPiano-SF2-V3+20200602.tar.xz  
```

## Install

```
pip install midiSynth==0.2
```

## Usage

1. Without soundfont:

```
from midiSynth.synth import MidiSynth
midi_synth = MidiSynth()
midi_synth.play_midi('test.mid')
midi_synth.midi2audio('test.mid', 'output.mp3')
```
2. Use other soundfont: 

```
path_sf = PATH_OF_THE_SF2_FILE
midi_synth = MidiSynth(path_sf = path_sf)
midi_synth.play_midi('test.mid')
midi_synth.midi2audio('test.mid', 'output.mp3')
```


## License
1. `test.mid` comes from [Ever So Blue - Onthou](https://www.youtube.com/watch?v=YhXRyOl5pi0), and I don't own the copyright.
2. The soundfont file comes from [FreePats](https://freepats.zenvoid.org/Piano/acoustic-grand-piano.html), and again I don't own the copyright. The author is Alexander Holm, axeldenstore (at) gmail (dot) com, and the original License is Creative Commons Attribution 3.0 license.

