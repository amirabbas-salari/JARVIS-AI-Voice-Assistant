import soundfile as sf

from kokoro import KPipeline

from config import (
    TTS_LANGUAGE,
    TTS_VOICE,
)


class TextToSpeech:

    def __init__(self):

        print("Loading TTS model...")

        self.pipeline = KPipeline(
            lang_code=TTS_LANGUAGE
        )

    def speak(self, text):

        print("🔊 Generating voice...")

        generator = self.pipeline(
            text,
            voice=TTS_VOICE
        )

        audio_parts = []

        for _, _, audio in generator:
            audio_parts.append(audio)

        if not audio_parts:
            raise RuntimeError(
                "TTS did not generate any audio."
            )

        audio = audio_parts[0]

        output_file = "response.wav"

        sf.write(
            output_file,
            audio,
            24000
        )

        return output_file