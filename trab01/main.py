import os

from binary_utils.binary_utils import BinaryUtils

if __name__ == '__main__':
    binary_utils = BinaryUtils()

    binary_utils.safe_copy('./image01.jpeg')
    binary_utils.safe_copy('./file01.pdf')
    binary_utils.safe_copy('./text01.txt')

    text = b'## Entregar 1kg de droga na Rua X ##'
    start = os.path.getsize('./image01_safecopy.jpeg')
    end = start + len(text) - 1

    binary_utils.write('./image01_safecopy.jpeg', text, start)
    print(binary_utils.diff('./image01.jpeg', './image01_safecopy.jpeg'))
