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
                img.resize((320, int(img.height * 320 / img.width)))
            else:
                img.resize((int(img.width * 320 / img.height), 320))

        canvas = Image.new('RGB', (int(sizeTaken*1.075), int(sizeTaken*1.075)), (255, 255, 255))

        # calcul la position ou mettre limage
        if sizeTaken == img.width:
            pos = ((int(0.075 * sizeTaken), int(sizeTaken / 2 - img.height / 2)))
        else:
            pos = ((int(sizeTaken / 2 - img.width / 2), int(0.075 * sizeTaken)))

        canvas.paste(img, pos)
        canvas.save(path + '/' + imgstr)
        i += 1
    print('done')


if __name__ == '__main__':
    modify_image('Logos/Logos_epg.best')
