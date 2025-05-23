import speech_recognition as sr

def ouvir_microfone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Ouvindo...")
        r.adjust_for_ambient_noise(source, duration=1)  # melhor calibração
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
        except sr.WaitTimeoutError:
            print("⏱️ Tempo esgotado esperando fala.")
            return ""

    try:
        texto = r.recognize_google(audio, language='pt-BR')
        print(f"🗣️ Você disse: {texto}")
        return texto.lower()
    except sr.UnknownValueError:
        print("❌ Não entendi o que você disse.")
        return ""
    except sr.RequestError:
        print("❌ Erro de conexão com o serviço de reconhecimento.")
        return ""
