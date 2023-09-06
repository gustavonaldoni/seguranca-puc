import os

from binary_utils.binary_utils import BinaryUtils

if __name__ == '__main__':
    binary_utils = BinaryUtils()

    binary_utils.safe_copy('./image01.jpeg')
    binary_utils.safe_copy('./file01.pdf')
    binary_utils.safe_copy('./text01.txt')

    binary_utils.write('./text01_safecopy.txt', b'#######', os.path.getsize('./text01_safecopy.txt'))