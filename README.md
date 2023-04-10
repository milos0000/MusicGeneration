# MusicGeneration
Generating music using LSTM reccurent neural network combined with some music heuristics:

## Process
I used POP909 dataset and music21 set of toolkit to feed my lstm neural network for generating music. 
First thing I did was filtering the dataset. Only songs used from this dataset are those (I guess) basic ones which have standard names (001.mid for example). Then I filtered only melodies, dropping the bridge and piano parts from each song. I wrote python scripts for those tasks.

All songs are MIDI files, and music21 can handle those files very well, so I used it to load all songs in special structures (streams containing notes).
The next thing on schedule was transforming those note sequences to some form of input that can be processed by network. One-hot encoding was easy choice.

## Network architecture:
LSTM(1024)

Dropout(0.25)

Dense(328)

Dense(softmax)

# Flow 
Program prompts user for: 

scale (which user wants the song to be composed in)

seed (first 16 notes of a song)

progression (4 chords cycle)

These things are hard-coded right now but will be changed when the project is over.

## Heuristics 
1. Walking up and down to chords (based on progression)
2. Sanctioning notes that are not in the scale except when they are used for chromatic walk. Program chooses another note from scale after sanction.
3. Sanctioning notes that are frequently repeated (also by choosing random note from scale instead).

## Dataset
https://arxiv.org/abs/2008.07142
