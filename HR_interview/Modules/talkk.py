from threading import Thread
import mj
def patnaik():
    mj.stt("hello introduce yourself within 30 seconds")
    import sounddevice as sd
    from scipy.io.wavfile import write
    import wavio as wv
    freq = 44100
    duration = 30
    recording = sd.rec(int(duration * freq),
                       samplerate=freq, channels=2)
    sd.wait()

    write("talk.wav", freq, recording)

    wv.write("talk1.wav", recording, freq, sampwidth=2)
    mj.stt("thats a great introduction lets proceed")

h6 = Thread(target=patnaik)
h6.start()
