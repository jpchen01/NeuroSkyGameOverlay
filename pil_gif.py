from PIL import Image
import glob

def gen_frame(path):
    im = Image.open(path)
    alpha = im.getchannel('A')

    # Convert the image into P mode but only use 255 colors in the palette out of 256
    im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)

    # Set all pixel values below 128 to 255 , and the rest to 0
    mask = Image.eval(alpha, lambda a: 255 if a <=128 else 0)

    # Paste the color of index 255 and use alpha as a mask
    im.paste(255, mask)

    # The transparency index is 255
    im.info['transparency'] = 255

    return im


if __name__ == '__main__':
    frames = []
    for filename in glob.glob("./WispEffects/*"):
        frames.append(gen_frame(filename))
        print(filename)

    frames[0].save('WispyEffect.gif', save_all=True, append_images=frames[1:], disposal=2, loop=0, duration=20)