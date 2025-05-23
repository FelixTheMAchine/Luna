# voz/fala.py
import os
import json
from playsound import playsound

# Caminho base para os áudios
base_path = r"D:\luna_ai\vozBase"

# Carrega o mapeamento de comandos para arquivos de áudio
with open(os.path.join(os.path.dirname(__file__), "comandos_audio.json"), encoding="utf-8") as f:
    comandos_audio = json.load(f)

def falar_luna(chave):
    """Toca o áudio correspondente ao comando de fala da Luna."""
    arquivo = comandos_audio.get(chave, "LunaNaoEntendeu.mp3")
    caminho_completo = os.path.join(base_path, arquivo)

    if not os.path.exists(caminho_completo):
        print(f"❌ Arquivo de áudio não encontrado: {caminho_completo}")
        return

    print(f"🎵 Luna: tocando '{arquivo}'")
    playsound(caminho_completo)
