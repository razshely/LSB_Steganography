import argparse
import sys
import numpy as np
import PIL.Image
import random

parser = argparse.ArgumentParser(description="Image Steganography")
parser.add_argument('-e', type=str, help="To embed a message in the image", nargs='+')
parser.add_argument('-f', help="To pass .png (Image) file")
parser.add_argument('-x', help="To extract the message from the image.", action="store_true")
args = parser.parse_args()

STOPM = "$@FINISH@$"


# Can be support to hiiden files too
# just for file that can be storage in the image

def main():
    if not args.f:
        print("Please enter a file name.")
        print("[*] Type -h for help.")
        sys.exit(1)
    else:
        if args.e and not args.x:
            args.e = ' '.join(args.e[i] for i in range(len(args.e)))
            if ".png" in args.f:
                image = PIL.Image.open(args.f, 'r')
                img_arr = np.array(list(image.getdata()))
                w, h = image.size

                if image.mode == 'P':
                    print("[-] Not support yet")
                    sys.exit(1)
                # Support on only "RGBA" and "RGB" mode
                numOflevel = 4 if image.mode == "RGBA" else 3

                sumOfPixels = img_arr.size // numOflevel
                args.e += STOPM
                print(args.e)
                byte_massage = ''.join(f"{ord(ch):08b}" for ch in args.e)

                if len(byte_massage) > sumOfPixels:
                    print("Not enough space")
                    sys.exit(1)

                index = 0
                for i in range(sumOfPixels):
                    for j in range(numOflevel):
                        if index < len(byte_massage):
                            img_arr[i][j] = int(bin(img_arr[i][j])[2:-1] + byte_massage[index], 2)
                            index += 1

                img_arr = img_arr.reshape((h, w, numOflevel))
                res = PIL.Image.fromarray(img_arr.astype('uint8'), image.mode)
                res.save("end" + str(random.randrange(10, 99)) + ".png")

                if image.mode == 'P':
                    print("[-] Not support yet")
                    sys.exit(1)
                # Support on only "RGBA" and "RGB" mode
                numOflevel = 4 if image.mode == "RGBA" else 3
                sumOfPixels = img_arr // numOflevel
            elif ".mp3" in args.f:
                print("[-] Not support yet")
                sys.exit(1)
        elif args.x and not args.e:
            if ".png" in args.f:
                image = PIL.Image.open(args.f, 'r')
                img_arr = np.array(list(image.getdata()))

                if image.mode == 'P':
                    print("[-] Not support yet")
                    sys.exit(1)

                numOflevel = 4 if image.mode == "RGBA" else 3
                sumOfPixels = img_arr.size // numOflevel

                hidden = [bin(img_arr[i][j])[-1] for i in range(sumOfPixels) for j in range(numOflevel)]
                hidden = ''.join(hidden)
                hidden = [hidden[i:i + 8] for i in range(0, len(hidden), 8)]
                hidden = [chr(int(hidden[i], 2)) for i in range(len(hidden))]
                hidden = ''.join(hidden[i] for i in range(len(hidden)))
                index = hidden.find(STOPM)
                print("The secret massage is: " + hidden[:index])
            elif ".mp3" in args.f:
                print("[-] Not support yet")
                sys.exit(1)
    sys.exit(0)


if __name__ == '__main__':
    main()
