caminho_arquivo_inicial = './teste.txt'
caminho_arquivo_destino = './teste_criptografado.txt'

caminho_arquivo_descriptografado = './teste_descriptografado.txt'

chave = 5

def criptografar(caminho_arquivo_inicial: str, caminho_arquivo_destino: str) -> bool:
    arquivo_inicial = open(caminho_arquivo_inicial, mode='rt')
    arquivo_destino = open(caminho_arquivo_destino, mode='w')

    caractere = arquivo_inicial.read(1)

    while caractere:
        caractere_criptografado = chr(ord(caractere) + chave)
        arquivo_destino.write(caractere_criptografado)

        caractere = arquivo_inicial.read(1)

    arquivo_inicial.close()
    arquivo_destino.close()

    return True

def descriptografar(caminho_arquivo_criptografado: str, caminho_arquivo_descriptografado: str) -> bool:
    arquivo_criptografado = open(caminho_arquivo_criptografado, mode='rt')
    arquivo_descriptografado = open(caminho_arquivo_descriptografado, mode='w')

    caractere = arquivo_criptografado.read(1)

    while caractere:
        caractere_descriptografado = chr(ord(caractere) - chave)
        arquivo_descriptografado.write(caractere_descriptografado)

        caractere = arquivo_criptografado.read(1)

    arquivo_criptografado.close()
    arquivo_descriptografado.close()

    return True

if __name__ == '__main__':
    criptografar(caminho_arquivo_inicial, caminho_arquivo_destino)
    descriptografar(caminho_arquivo_destino, caminho_arquivo_descriptografado)