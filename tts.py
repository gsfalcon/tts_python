import os
import random

userText = input("Digite o texto a ser convertido em .mp3: ")
idGen = random.randint(1111, 9999)

os.system('edge-tts --voice pt-BR-AntonioNeural --text "{}" --write-media audio_{}.mp3'.format(userText, idGen))

print("\nArquivo de áudio salvo em: 'tts_python/audio_{}.mp3'\n".format(idGen))