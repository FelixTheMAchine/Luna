# main.py
from voz.reconhecimento import ouvir_microfone
from voz.fala import falar_luna
from sistema.comandos import executar_acao
import time

def main():
    falar_luna("iniciar")
    ativo = True

    while True:
        falar_luna("oi")
        comando = ouvir_microfone()

        if not comando:
            continue

        print(f"🗣️ Você disse: {comando}")

        if not comando.startswith("luna"):
            falar_luna("não entendeu o comando")
            continue

        comando_sem_prefixo = comando.replace("luna", "", 1).strip()

        if any(palavra in comando_sem_prefixo for palavra in ["desligar", "parar", "pausar programa", "sair"]):
            falar_luna("desligar")
            break

        elif any(palavra in comando_sem_prefixo for palavra in ["iniciar", "continuar", "voltar"]):
            if not ativo:
                falar_luna("voltou")
                ativo = True
            else:
                falar_luna("iniciar")

        elif ativo:
            executar_acao("luna " + comando_sem_prefixo)

        time.sleep(1)

if __name__ == "__main__":
    main()
