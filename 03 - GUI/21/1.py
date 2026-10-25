import pysynth as ps

# تعریف یک ملودی ساده
melody = [
    ("c4", 4),
    ("e4", 4),
    ("g4", 4),
    ("c5", 4),
    ("e5", 4),
    ("g5", 4),
    ("c6", 2),
    ("g5", 2),
    ("e5", 2),
    ("c5", 2),
    ("g4", 2),
    ("e4", 2),
    ("c4", 1),
]

# ساخت آهنگ
ps.make_wav(melody, fn="simple_song.wav")
