import mido
import os
# Define the file paths for your input and output directories
input_dir = "/home/milos/Desktop/MY_POP/"
output_dir = "/home/milos/Desktop/POPMELODY/"

# Loop through all MIDI files in the input directory
for file_name in os.listdir(input_dir):
    # Skip any files that are not MIDI files
    if not file_name.endswith(".mid"):
        continue

    # Load the MIDI file
    file_path = os.path.join(input_dir, file_name)
    midi = mido.MidiFile(file_path)

    # Create a new MIDI file containing only the melody part
    melody_track = mido.MidiTrack()
    for track in midi.tracks:
        for msg in track:
            # Keep only the messages in the melody track (i.e. track number 0)
            if msg.type == "program_change" and msg.channel == 0:
                melody_track.append(msg)
            elif msg.type in ["note_on", "note_off"] and track.name == "MELODY":
                melody_track.append(msg)

    # Write the new MIDI file to the output directory
    output_path = os.path.join(output_dir, file_name)
    midi.tracks = [melody_track]
    midi.save(output_path)

