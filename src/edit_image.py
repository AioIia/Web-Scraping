from PIL import Image
import os


def modify_image(path):
    i = 0
    n = len(os.listdir(path))
    # pour chaque image dans le dossier fais le truc
    for g in range(len(os.listdir(path))):
        # affiche la progresseion
        print(f"{str(round(100 * i / n, 2))} %")

        # avoir le path de limage
        imgstr = str(os.listdir(path)[g])
        # ouvre limage
        img = Image.open(path + '/' + imgstr)

        sizeTaken = max(img.size)

        if sizeTaken < 320:
            if sizeTaken == img.width:
                img = img.resize((int(320*0.85), int(img.height*320/img.width*0.85)))
            else:
                img = img.resize((int(img.width * 320 / img.height*0.85), int(320*0.85)))
            sizeTaken = 320


        canvas = Image.new('RGB', (sizeTaken, sizeTaken), (255, 255, 255))

        # calcul la position ou mettre limage
        if max(img.size) == img.width:
            pos = (int(img.width*0.075), int(sizeTaken / 2 - img.height / 2))
        else:
            pos = ((int(sizeTaken / 2 - img.width / 2), int(img.height*0.075)))

        canvas.paste(img, pos)
        canvas.save(path + '/' + imgstr)
        i += 1
    print('done')


if __name__ == '__main__':
    modify_image('data/logos/logos_epg.best')
