import sounddevice as sd
import soundfile as sf


def play_audio(path):

    audio, rate = sf.read(path)

    sd.play(
        audio,
        rate
    )

    sd.wait()