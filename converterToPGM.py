from PIL import Image
import numpy as np

def getImageGrayMatriz(filename):
    im = Image.open(filename).convert('L')
    return np.array(im)

def writePGMImage(im, filename):
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write('P2\n')
        file.write(f'{im.shape[1]} {im.shape[0]}\n')
        file.write(f'{np.max(im)}\n')
        for line in im:
            file.write(' '.join(line.astype(str)) + '\n')
        file.write('\n')

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Convert image to pgm')
    parser.add_argument('img_filename', metavar='img_filename', type=str, nargs=1,
                        help='Image filename to convert')
    parser.add_argument('out_filename', metavar='out_filename', type=str, nargs=1,
                        help='output name')
    args = parser.parse_args()
    img_filename = args.img_filename[0]
    out_filename = args.out_filename[0]

    im = getImageGrayMatriz(img_filename)
    writePGMImage(im, out_filename)
