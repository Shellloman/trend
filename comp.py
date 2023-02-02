from moviepy.editor import *
from moviepy.video.fx.scroll import scroll
from moviepy.video.fx.resize import resize
from moviepy.video.fx.rotate import rotate

audio = "songs/tiktok_song.m4a"

audio_clip = CompositeAudioClip([
        AudioFileClip(audio).subclip(60+59-10, 120+29),
        AudioFileClip(audio).subclip(120+45, 120+45+60).set_start(40)
    ])

audio_clip.write_audiofile('songs/holy.mp3', fps=AudioFileClip(audio).fps)