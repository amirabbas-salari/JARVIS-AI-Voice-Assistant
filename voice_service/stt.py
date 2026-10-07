from faster_whisper import WhisperModel

from config import (
    WHISPER_MODEL,
    DEVICE,
    COMPUTE_TYPE,
    STT_LANGUAGE,
)


class SpeechRecognizer:

    def __init__(self):

        print("Loading Whisper model...")

        self.model = WhisperModel(
            WHISPER_MODEL,
            device=DEVICE,
            compute_type=COMPUTE_TYPE,
        )

    def transcribe(self, audio_file):

        segments, info = self.model.transcribe(
            audio_file,

            language=STT_LANGUAGE,

            beam_size=5,

            vad_filter=True,

            condition_on_previous_text=False,

            temperature=0.0,

        )

        text_parts = []

        for segment in segments:

            text = segment.text.strip()

            if text:

                text_parts.append(text)

        return " ".join(text_parts).strip()