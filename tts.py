
import os
import random

texto = input("Por favor, digite o texto a ser convertido em áudio: ")

n_aleat = random.randint(1111, 9999)



os.system('edge-tts --voice pt-BR-AntonioNeural --text "{}" --write-media audio{}.mp3'.format(texto, n_aleat))