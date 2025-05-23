from voz.fala import falar_luna
import pyautogui
import re
import time
import webbrowser
import subprocess

def executar_acao(comando):
    comando = comando.lower().strip()

    if not comando.startswith("luna"):
        falar_luna("entender")
        return

    comando_sem_luna = comando[len("luna"):].strip()

    def repetir_tecla(tecla, vezes, delay=0.1):
        for _ in range(vezes):
            if isinstance(tecla, tuple):
                pyautogui.hotkey(*tecla)
            else:
                pyautogui.press(tecla)
            time.sleep(delay)

    # === COMANDOS MULTIMÍDIA (já existentes) ===
    match_aumentar = re.search(r'(?:aumentar|subir|levantar) (?:volume )?(?:em )?(\d+)', comando_sem_luna)
    match_diminuir = re.search(r'(?:diminuir|abaixar|baixar) (?:volume )?(?:em )?(\d+)', comando_sem_luna)

    if any(x in comando_sem_luna for x in ["próxima música", "pula", "pular música", "avançar", "próximo"]):
        falar_luna("próxima música")
        pyautogui.hotkey('ctrl', 'right')

    elif any(x in comando_sem_luna for x in ["música anterior", "volta", "voltar música", "anterior"]):
        falar_luna("voltar")
        pyautogui.hotkey('ctrl', 'left')

    elif any(x in comando_sem_luna for x in ["aleatório", "embaralhar", "shuffle"]):
        falar_luna("aleatório")
        pyautogui.hotkey('ctrl', 's')

    elif any(x in comando_sem_luna for x in ["repetir", "loop"]):
        falar_luna("repetir música")
        pyautogui.hotkey('ctrl', 'r')

    elif any(x in comando_sem_luna for x in ["despausar", "play", "tocar", "despausar musica"]):
        falar_luna("iniciar")
        pyautogui.press('space')

    elif any(x in comando_sem_luna for x in ["pausar", "pause", "parar", "stop"]):
        falar_luna("desligar")
        pyautogui.press('space')

    elif match_aumentar:
        qtd = int(match_aumentar.group(1))
        falar_luna("subir volume")
        repetir_tecla(('ctrl', 'up'), qtd)

    elif match_diminuir:
        qtd = int(match_diminuir.group(1))
        falar_luna("baixar volume")
        repetir_tecla(('ctrl', 'down'), qtd)

    elif "volume no máximo" in comando_sem_luna:
        falar_luna("subir volume")
        repetir_tecla(('ctrl', 'up'), 50, delay=0.05)

    elif "volume no mínimo" in comando_sem_luna or "volume zero" in comando_sem_luna:
        falar_luna("baixar volume")
        repetir_tecla(('ctrl', 'down'), 50, delay=0.05)

    # === NOVOS COMANDOS DE JANELA/SISTEMA ===

    elif "minimizar" in comando_sem_luna:
        falar_luna("desligar")
        pyautogui.hotkey("win", "down")

    elif "maximizar" in comando_sem_luna:
        falar_luna("iniciar")
        pyautogui.hotkey("win", "up")

    elif "fechar janela" in comando_sem_luna or "fechar programa" in comando_sem_luna:
        falar_luna("desligar")
        pyautogui.hotkey("alt", "f4")

    elif "alternar janela" in comando_sem_luna or "mudar de janela" in comando_sem_luna:
        falar_luna("iniciar")
        pyautogui.hotkey("alt", "tab")

    elif "explorador de arquivos" in comando_sem_luna or "abrir arquivos" in comando_sem_luna:
        falar_luna("iniciar")
        subprocess.Popen("explorer")

    elif "abrir calculadora" in comando_sem_luna:
        falar_luna("iniciar")
        subprocess.Popen("calc")

    elif "abrir bloco de notas" in comando_sem_luna:
        falar_luna("iniciar")
        subprocess.Popen("notepad")

    # === COMANDOS DE NAVEGADOR ===

    elif "abrir youtube" in comando_sem_luna:
        falar_luna("iniciar")
        webbrowser.open("https://www.youtube.com")

    elif "abrir google" in comando_sem_luna:
        falar_luna("iniciar")
        webbrowser.open("https://www.google.com")

    elif "abrir github" in comando_sem_luna:
        falar_luna("iniciar")
        webbrowser.open("https://github.com")


    else:
        falar_luna("não entendeu o comando")
