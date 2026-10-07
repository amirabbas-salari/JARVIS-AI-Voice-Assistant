import queue
import time

import numpy as np
import sounddevice as sd

from config import (
    SAMPLE_RATE,
    CHANNELS,
    CHUNK_SIZE,
    PRE_ROLL_MS,
    SILENCE_LIMIT_MS,
    MIN_SPEECH_MS,
    MAX_UTTERANCE_MS,
)


class AudioRecorder:

    def __init__(self, vad):
        self.vad = vad

        self.audio_queue = queue.Queue()

        self.stream = None

    def _callback(self, indata, frames, time_info, status):
        if status:
            print(f"Audio status: {status}")

        audio = indata[:, 0].copy()

        self.audio_queue.put(audio)

    def record_until_silence(self):
        """
        ضبط از شروع صحبت تا پایان جمله.

        مکث کوتاه باعث قطع ضبط نمی‌شود.
        """

        self.vad.reset()

        self.audio_queue = queue.Queue()

        pre_roll_chunks = []

        speech_started = False

        speech_chunks = []

        speech_start_time = None
        last_speech_time = None

        chunk_duration_ms = (
            CHUNK_SIZE / SAMPLE_RATE
        ) * 1000

        max_pre_roll_chunks = max(
            1,
            int(PRE_ROLL_MS / chunk_duration_ms)
        )

        print("🎤 Listening...")

        self.stream = sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype="float32",
            blocksize=CHUNK_SIZE,
            callback=self._callback,
        )

        self.stream.start()

        try:

            while True:

                chunk = self.audio_queue.get()

                now = time.monotonic()

                is_speech = self.vad.is_speech(chunk)

                # ---------------------------------
                # هنوز صحبت شروع نشده
                # ---------------------------------

                if not speech_started:

                    pre_roll_chunks.append(chunk)

                    if len(pre_roll_chunks) > max_pre_roll_chunks:
                        pre_roll_chunks.pop(0)

                    if is_speech:

                        speech_started = True

                        speech_start_time = now
                        last_speech_time = now

                        speech_chunks.extend(
                            pre_roll_chunks
                        )

                        pre_roll_chunks.clear()

                        print("✅ Speech detected")

                    continue

                # ---------------------------------
                # صحبت شروع شده
                # ---------------------------------

                speech_chunks.append(chunk)

                if is_speech:

                    last_speech_time = now

                # ---------------------------------
                # پایان صحبت
                # ---------------------------------

                silence_duration_ms = (
                    now - last_speech_time
                ) * 1000

                utterance_duration_ms = (
                    now - speech_start_time
                ) * 1000

                # حداقل مدت صحبت
                if (
                    utterance_duration_ms >= MIN_SPEECH_MS
                    and silence_duration_ms >= SILENCE_LIMIT_MS
                ):

                    print("🛑 Speech ended")

                    break

                # جلوگیری از ضبط بی‌نهایت
                if utterance_duration_ms >= MAX_UTTERANCE_MS:

                    print("⏱️ Maximum utterance duration reached")

                    break

        finally:

            self.stream.stop()
            self.stream.close()

            self.stream = None

        if not speech_chunks:
            return None

        audio = np.concatenate(speech_chunks)

        return audio