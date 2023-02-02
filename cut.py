import skimage as sk
from os import listdir

folder = 'superman/'
files = sorted(listdir(folder+'raws/'))

for k, file in enumerate(files):
    img = sk.io.imread(folder+'raws/'+file)
    size, _, _ = img.shape

    sk.io.imsave(f'{folder}/imgs/img{0 if k*4+0 < 10 else ""}{k*4 + 0}.png', img[:size // 2, :size // 2, :])
    sk.io.imsave(f'{folder}/imgs/img{0 if k*4+1 < 10 else ""}{k*4 + 1}.png', img[size // 2:, :size // 2, :])
    sk.io.imsave(f'{folder}/imgs/img{0 if k*4+2 < 10 else ""}{k*4 + 2}.png', img[:size // 2, size // 2:, :])
    sk.io.imsave(f'{folder}/imgs/img{0 if k*4+3 < 10 else ""}{k*4 + 3}.png', img[size // 2:, size // 2:, :])
