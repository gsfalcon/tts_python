import os
import random

userText = input("Digite o texto a ser convertido em .mp3: ")
idGen = random.randint(100, 999)

cleanedText = userText.replace("\n", " ").replace("\r", " ")

# Utilize o caminho completo para evitar problemas de resolução de diretório
output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), f'../tts_python/audio_{idGen}.mp3'))

try:
    os.system(f'edge-tts --voice pt-BR-AntonioNeural --pitch=-5Hz --rate=0.97 --text "{cleanedText}" --write-media "{output_path}"')
    print(f"\nArquivo de áudio salvo em: '{output_path}'\n")
except Exception as e:
    print("Erro ao salvar o arquivo de áudio:", e)

# pip install pipx
# pipx install edge-tts