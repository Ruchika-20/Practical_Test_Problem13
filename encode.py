# Importing the required libraries
from PIL import Image
import sys
import argparse
import qrcode

parser = argparse.ArgumentParser(description='Steganography')
subparser = parser.add_subparsers(dest='command')

merge = subparser.add_parser('merge')
merge.add_argument('--input_img_to_encode', required=True, help='InputImage path')  #args change kiye the bs main
merge.add_argument('--output', required=True, help='Output path')
args = parser.parse_args()

secret_code = input("Enter the secret message:")
qr = qrcode.make(secret_code)

im = Image.open(args.input_img_to_encode)
qr = qr.convert('RGB')

# Resizing the iamge and qrcode
width,height = None,None
if(im.size[0] > qr.size[0]):
   width = im.size[0]
else:
   width = qr.size[0]

if(im.size[1] > qr.size[1]):
   height = im.size[1]
else:
    height = qr.size[1]

im = im.resize((width,height))
qr = qr.resize((width,height))

pix = im.load()
qrp = qr.load()

if im.size < qr.size:
	print("error")
	sys.exit()

for x in range(qr.size[0]):
	for y in range(qr.size[1]):
		pi = pix[x,y]
		change = False
		if qrp[x,y][0]:
			if sum(pi)%2:
				continue
			else:
				change = True
		else:
			if sum(pi)%2:
				change = True
			else:
				continue
		if change:
			pix[x,y] = (pi[0]-1, pi[1], pi[2])

im.save(args.output)
