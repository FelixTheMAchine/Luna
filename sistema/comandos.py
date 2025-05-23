from voz.fala import falar_luna
import pyautogui
import re
import time

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

    elif any(x in comando_sem_luna for x in ["despausar", "play", "tocar"]):
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

    elif any(x in comando_sem_luna for x in ["volume no máximo", "volume máximo"]):
        falar_luna("subir volume")
        repetir_tecla(('ctrl', 'up'), 50, delay=0.05)

    elif any(x in comando_sem_luna for x in ["volume no mínimo", "volume zero"]):
        falar_luna("baixar volume")
        repetir_tecla(('ctrl', 'down'), 50, delay=0.05)

    else:
        falar_luna("não entendeu o comando")