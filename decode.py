from PIL import Image
import argparse

parser = argparse.ArgumentParser(description='Steganography')
subparser = parser.add_subparsers(dest='command')
merge = subparser.add_parser('unmerge')

# Adding arguments to fed as an input for decoding
merge.add_argument('--input_img_to_decode', required=True, help='EncodedImage path')
merge.add_argument('--output', required=True, help='Output path')
args = parser.parse_args()

im = Image.open(args.input_img_to_decode)
pix = im.load()

for x in range(im.size[0]):
	for y in range(im.size[1]):
		if sum(pix[x,y])%2:
			pix[x,y] = (255, 255, 255)
		else:
			pix[x,y] = (0, 0, 0)

im.save(args.output)
