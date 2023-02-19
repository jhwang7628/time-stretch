from pathlib import Path

import librosa
import soundfile as sf

test_wav = Path("../data/FUNK-GROOVE-HORNS-CATCHY_AdobeStock_497992046.wav")

assert test_wav.is_file()

y, sr = librosa.load(test_wav)

print(y)

sf.write("./output1.wav", y, sr)

y_slow = librosa.effects.time_stretch(y, rate=0.5)

sf.write("./output2.wav", y_slow, sr)

y_slowest = librosa.effects.time_stretch(y, rate=0.25)

sf.write("./output3.wav", y_slowest, sr)
