from threading import Thread

def rec():
    import sounddevice as sd
    from scipy.io.wavfile import write
    import wavio as wv
    freq = 44100
    duration = 102
    recording = sd.rec(int(duration * freq),
                       samplerate=freq, channels=2)
    sd.wait()

    write("recording0.wav", freq, recording)

    wv.write("recording1.wav", recording, freq, sampwidth=2)
    from pydub import AudioSegment
    from pydub.utils import make_chunks

    myaudio = AudioSegment.from_file("recording1.wav", "wav")
    chunk_length_ms = 20000
    chunks = make_chunks(myaudio, chunk_length_ms)

    for i, chunk in enumerate(chunks):
        chunk_name = "c{0}.wav".format(i)
        chunk.export(chunk_name, format="wav")

t1 = Thread(target=rec)
t1.start()



