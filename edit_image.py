from PIL import Image
import os

def modify_image(path):
    i = 0
    n = len(os.listdir(path))
    #pour chaque image dans le dossier fais le truc
    for g in range(len(os.listdir(path))):
        #affiche la progresseion
        print(f"{str(round(100*i/n, 2))} %")

        #avoir le path de limage
        imgstr = str(os.listdir(path)[g])
        #ouvre limage
        img = Image.open(path + '/' + imgstr)

        #prend le premier pixel pour en faire un carre
        rgb_im = img.convert('RGB')
        r, g, b = rgb_im.getpixel((1, 1))
        sizeTaken = max(img.size)
        canvas = Image.new('RGB', (sizeTaken, sizeTaken), (r, g, b))

        #calcul la position ou mettre limage
        if sizeTaken == img.width:
            pos = ((0, int(sizeTaken/2-img.height/2)))
        else:
            pos = ((int(sizeTaken/2-img.width/2), 0))

        canvas.paste(img, pos)
        canvas.save(path+'/'+imgstr)
        i += 1
    print('done')