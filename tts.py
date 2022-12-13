# https://github.com/rany2/edge-tts

import os
import random

texto = input("Digite o texto a ser convertido em .mp3: ")
n_aleat = random.randint(1111, 9999)

os.system('edge-tts --voice pt-BR-AntonioNeural --text "{}" --write-media audio_{}.mp3'.format(texto, n_aleat))

print("\nArquivo de áudio salvo em: 'tts_python/audio_{}.mp3'\n".format(n_aleat))