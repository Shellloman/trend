from moviepy.editor import *
from moviepy.video.fx.scroll import scroll
from moviepy.video.fx.resize import resize
from moviepy.video.fx.rotate import rotate


wall = 'templates/wallpaper.jpg'


wall_clip = ImageClip(wall).set_duration(3).set_start(0)
wall_clip = scroll(wall_clip, 1920, 1080, 15, 0, 0, 0)

clips = [
    ImageClip('imgs/img3.png').set_duration(3).set_start(0).set_position((14, 300)),
    ImageClip('imgs/img7.png').set_duration(3).set_start(0).set_position((512+28+14, 300)),
    ImageClip('imgs/img11.png').set_duration(3).set_start(0).set_position((14, 300+28+512)),
    ImageClip('imgs/img15.png').set_duration(3).set_start(0).set_position((512+28+14, 300+28+512)),
    ImageClip('imgs/img19.png').set_duration(3).set_start(0).set_position(('center', 300+(512+28)*2)),
    TextClip("Which one\nis the best ?",
             color='white', font="Eras-Bold-ITC", kerning=5, fontsize=105, stroke_color='Black', stroke_width=3)
    .set_duration(3).set_start(0).set_position(('center', 50), relative=False)
]

final_clip = CompositeVideoClip([wall_clip, *clips], size=(1080, 1920))

final_clip.write_videofile('output/comp.mp4', fps=10)
