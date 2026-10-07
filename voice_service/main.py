from pathlib import Path

import soundfile as sf

from audio import AudioRecorder
from vad import VoiceDetector
from stt import SpeechRecognizer
from n8n_client import N8NClient
from config import N8N_WEBHOOK_URL
from tts import TextToSpeech
from player import play_audio

BASE_DIR = Path(__file__).resolve().parent

RECORDINGS_DIR = BASE_DIR / "recordings"

RECORDINGS_DIR.mkdir(
    exist_ok=True
)


def main():

    # -----------------------------
    # Load models
    # -----------------------------

    vad = VoiceDetector()

    whisper = SpeechRecognizer()

    recorder = AudioRecorder(vad)
    
    n8n = N8NClient(N8N_WEBHOOK_URL)

    print()
    print("=" * 50)
    print("        JARVIS Voice Service")
    print("=" * 50)
    print()
    print("Press Enter to speak")
    print("Press Ctrl+C to exit")
    print()


    try:

        while True:

            input("Press Enter to speak...")

            # -----------------------------
            # Record
            # -----------------------------

            audio = recorder.record_until_silence()

            if audio is None:

                print("❌ No speech detected")

                continue

            # -----------------------------
            # Save audio
            # -----------------------------

            filename = (
                RECORDINGS_DIR / "input.wav"
            )

            sf.write(
                filename,
                audio,
                16000
            )



            # -----------------------------
            # n8n
            # -----------------------------
            n8n = N8NClient(N8N_WEBHOOK_URL)
            
            
            # -----------------------------
            # Speech To Text
            # -----------------------------

            print("🧠 Transcribing...")

            text = whisper.transcribe(
                str(filename)
            )

            if not text:

                print("❌ Could not understand speech")

                continue

            print()
            print("JARVIS heard:")
            print(text)
            print()
            print("📡 Sending to n8n...")

            response = n8n.send_text(text)
            
            tts = TextToSpeech()

            audio_file = tts.speak(response)  

            play_audio(audio_file)

            print("🤖 JARVIS response:")
            print(response)

    except KeyboardInterrupt:

        print()
        print("👋 JARVIS stopped.")


if __name__ == "__main__":
    main()