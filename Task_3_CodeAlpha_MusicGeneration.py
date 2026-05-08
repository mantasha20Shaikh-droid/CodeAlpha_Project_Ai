# TASK 3 — Music Generation with AI
    # Install Libraries

print("----Task 3 - Music Generation with AI----")

!pip install music21 tensorflow numpy -q
    # AI Music Generator Code

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from music21 import stream, note, midi

   # Dummy Training Data
X = np.random.rand(100, 10, 1)
y = np.random.rand(100, 1)

   # Build Model
model = Sequential()

model.add(LSTM(128, input_shape=(10,1)))
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam')

   # Train Model
model.fit(X, y, epochs=5)

   # Generate Notes
generated = model.predict(np.random.rand(1,10,1))

  # Create MIDI File
s = stream.Stream()

for i in range(10):
    n = note.Note(int(generated[0][0]*50)+50)
    s.append(n)

mf = midi.translate.streamToMidiFile(s)
mf.open("generated_music.mid", 'wb')
mf.write()
mf.close()

print("Music Generated Successfully!")
  # Download Generated Music

from google.colab import files
files.download("generated_music.mid")
