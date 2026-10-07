import torch

from config import SAMPLE_RATE, VAD_THRESHOLD


class VoiceDetector:
    def __init__(self):
        print("Loading Silero VAD...")

        self.model, utils = torch.hub.load(
            repo_or_dir="snakers4/silero-vad",
            model="silero_vad",
            force_reload=False
        )

        self.model.eval()

        self.get_speech_timestamps = utils[0]

        self.sample_rate = SAMPLE_RATE
        self.threshold = VAD_THRESHOLD

    def is_speech(self, audio_chunk):
        """
        تشخیص می‌دهد chunk فعلی شامل speech است یا خیر.

        audio_chunk:
            numpy array یا torch tensor
        """

        if not isinstance(audio_chunk, torch.Tensor):
            audio_chunk = torch.from_numpy(audio_chunk)

        audio_chunk = audio_chunk.float()

        if audio_chunk.numel() == 0:
            return False

        # Silero VAD برای chunkهای کوتاه
        probability = self.model(
            audio_chunk,
            self.sample_rate
        ).item()

        return probability >= self.threshold

    def reset(self):
        """
        ریست کردن state مدل VAD
        """
        self.model.reset_states()