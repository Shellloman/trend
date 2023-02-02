from moviepy.editor import *
from moviepy.video.fx.scroll import scroll
from moviepy.video.fx.resize import resize
from moviepy.video.fx.rotate import rotate
from sys import argv

from os import listdir
from os.path import isfile

folder = argv[1]
print(folder)


def get_path(folder_, file_):
    if isfile(f'{folder_}/{file_}.jpg'):
        return f'{folder}/{file_}.jpg'
    elif isfile(f'{folder}/{file_}.png'):
        return f'{folder}/{file_}.png'
    else:
        raise Exception('unknow extension')


wall = get_path(folder, 'background')
first = get_path(folder, 'first')
audio = 'songs/tiktok_song.m4a'
imgs = sorted(listdir(f'{folder}/imgs/'))

frame_duration = 1
init_duration = 4
total_duration = init_duration*2+frame_duration*4*5

wall_clip = ImageClip(wall).set_duration(total_duration).set_start(0)
wall_clip = scroll(wall_clip, 1920, 1080, 20, 0, 0, 0)

angles = [12, -8, 5, -13]
texts = open(f'{folder}/text.txt', 'r').read().split('\n')
for i, t in enumerate(texts):
    texts[i] = t.replace('*', '\n')
print(texts)
pos = [(14, 300), (512+28+14, 300), (14, 300+28+512), (512+28+14, 300+28+512), ('center', 300+(512+28)*2)]

clips = [
    ImageClip(first).set_duration(init_duration).set_start(0).set_position("center"),
    TextClip(texts[0],
             color='white', font="Eras-Bold-ITC", kerning=5, fontsize=150,  stroke_color='Black', stroke_width=5)
    .set_duration(init_duration).set_start(0).set_position(('center', 0.06), relative=True)
]

for k, img in enumerate(imgs):
    clips.append(
        rotate(
            resize(
                ImageClip(f'{folder}/imgs/'+img).set_duration(frame_duration*(4 - k % 4))
                .set_start(init_duration+k*frame_duration).set_position("center"), 2
            ).add_mask(), angles[k % 4]
        )
    )

    if k % 4 == 3:
        clips.append(
            TextClip(texts[(k//4)+1],
                     color='white', font="Eras-Bold-ITC", kerning=5, fontsize=105, stroke_color='Black', stroke_width=3)
            .set_duration(frame_duration*4).set_start(init_duration+frame_duration*4*(k//4))
            .set_position(('center', 0.06), relative=True)
        )

        clips.append(
            ImageClip(f'{folder}/imgs/' + img).set_duration(init_duration)
            .set_start(init_duration+frame_duration*4*5).set_position(pos[k//4])
        )

clips.append(
    TextClip("Which one\nis the best ?",
             color='white', font="Eras-Bold-ITC", kerning=5, fontsize=105, stroke_color='Black', stroke_width=3)
    .set_duration(init_duration).set_start(init_duration+frame_duration*4*5).set_position(('center', 50))
)

final_clip = CompositeVideoClip([wall_clip, *clips], size=(1080, 1920))

if total_duration < 36:
    final_clip.audio = CompositeAudioClip(
        [AudioFileClip(audio).subclip(60+59-init_duration, 60+59-init_duration+total_duration)]
    )
else:
    final_clip.audio = CompositeAudioClip([
        AudioFileClip(audio).subclip(60+59-init_duration, 120+29),
        AudioFileClip(audio).subclip(120+45, 120+45+total_duration-30-init_duration).set_start(36)
    ])

final_clip.write_videofile('output/tiktok_fast_superman.mp4', fps=20)
