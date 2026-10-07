# ==========================================
# Audio
# ==========================================

SAMPLE_RATE = 16000
CHANNELS = 1

# هر chunk حدود 32ms
CHUNK_SIZE = 512


# ==========================================
# Voice Activity Detection
# ==========================================

VAD_THRESHOLD = 0.5

# مقدار صدای قبل از شروع speech که نگه داشته می‌شود
PRE_ROLL_MS = 300

# مدت سکوت برای پایان جمله
SILENCE_LIMIT_MS = 1500

# حداقل مدت صحبت معتبر
MIN_SPEECH_MS = 300

# حداکثر طول یک جمله
MAX_UTTERANCE_MS = 30000


# ==========================================
# Speech To Text
# ==========================================

WHISPER_MODEL = "large-v3"

# GPU
# DEVICE = "cuda"
# COMPUTE_TYPE = "float16"

# CPU
DEVICE = "cpu"
COMPUTE_TYPE = "int8"


# زبان صحبت کاربر
#
# fa = Persian
# en = English
# tr = Turkish
# de = German
# ar = Arabic
#
# اگر None باشد Whisper خودش زبان را تشخیص می‌دهد.
STT_LANGUAGE = "en"


# ==========================================
# Text To Speech
# ==========================================

# زبان صدای JARVIS
#
# فعلاً برای Kokoro:
# a = American English
# b = British English
#
TTS_LANGUAGE = "a"

# Voice مورد استفاده Kokoro
TTS_VOICE = "af_heart"


# ==========================================
# n8n
# ==========================================

N8N_WEBHOOK_URL = "http://localhost:5678/webhook-test/jarvis"