import io
from pathlib import Path

import librosa
import numpy as np
import soundfile as sf
import streamlit as st

test_wav = Path("../data/FUNK-GROOVE-HORNS-CATCHY_AdobeStock_497992046.wav")

assert test_wav.is_file()

st.title("Test streamlit page")

rate = st.slider("Slow down rate:", min_value=0.1, max_value=2.0, value=0.5,
                 step=0.1)

uploaded_file = st.file_uploader("Upload your audio file here:")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    tmp = io.BytesIO(bytes_data)
    data, samplerate = sf.read(tmp)
    data = np.array(data).transpose()
    print(data.shape, samplerate)

    st.text("Original:")
    st.audio(data, format="audio/wav", sample_rate=samplerate)

    st.text("Stretched:")
    data_slow = librosa.effects.time_stretch(data, rate=rate)
    st.audio(data_slow, format="audio/wav", sample_rate=samplerate)
    #sf.write("test.wav", data, samplerate)

#y, sr = librosa.load(test_wav)
#
#print(y)
#
#sf.write("./output1.wav", y, sr)
#
#y_slow = librosa.effects.time_stretch(y, rate=0.5)
#
#sf.write("./output2.wav", y_slow, sr)
#
#y_slowest = librosa.effects.time_stretch(y, rate=0.25)
#
#sf.write("./output3.wav", y_slowest, sr)
