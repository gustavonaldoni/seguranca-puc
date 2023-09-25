from binary_utils.binary_utils import BinaryUtils

if __name__ == '__main__':
    binary_utils = BinaryUtils()
    binary_utils.safe_copy('./final.png')

    posicao_inicial, posicao_final = (0x101C2, 0xB1C74)

    texto_binario = binary_utils.safe_copy_part(
        './final_safecopy.png', posicao_inicial, posicao_final, './resultado.pdf')
