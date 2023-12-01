# pip install pipx
# pipx install edge-tts
# pip install edge-tts

import os
import random

userText = input("Digite o texto a ser convertido em .mp3: ")
idGen = random.randint(100, 999)

os.system('edge-tts --voice pt-BR-AntonioNeural --pitch=-5Hz --rate=0.97 --text "{}" --write-media audio_{}.mp3'.format(userText, idGen))

print("\nArquivo de áudio salvo em: 'tts_python/audio_{}.mp3'\n".format(idGen))


#remover line breaks and paragraph breaks no input text
