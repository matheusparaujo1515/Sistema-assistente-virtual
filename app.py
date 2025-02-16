import speech_recognition as sr
import pyttsx3
import webbrowser
import time

def falar(texto):
# Converte texto em fala
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

def ouvir_comando():
# Captura o áudio do usuário e converte em texto
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        comando = recognizer.recognize_google(audio, language='pt-BR')
        print("Você disse: ", comando)
        return comando.lower()
    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
        return ""
    except sr.RequestError:
        print("Erro ao conectar-se ao serviço de reconhecimento.")
        return ""

def executar_comando(comando):
 # Executa uma ação com base no comando de voz
    sites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "facebook": "https://www.facebook.com",
        "globo": "https://www.globo.com",
        "mercado livre": "https://www.mercadolivre.com.br",
        "uol": "https://www.uol.com.br",
        "instagram": "https://www.instagram.com",
        "twitter": "https://twitter.com",
        "linkedin": "https://www.linkedin.com",
        "whatsapp": "https://web.whatsapp.com",
        "maps": "https://www.google.com/maps",
        "github": "https://www.github.com",
        "amazon": "https://www.amazon.com.br",
        "netflix": "https://www.netflix.com",
        "olx": "https://www.olx.com.br",
        "terra": "https://www.terra.com.br",
        "g1": "https://g1.globo.com",
        "tik tok": "https://www.tiktok.com",
        "folha": "https://www.folha.uol.com.br"
    }
    
    for site, url in sites.items():
        if comando in site or f"ir para {site}" in comando or f"abrir {site}" in comando:
            falar(f"Abrindo {site}")
            webbrowser.open(url)
            return
    
    locais = ["farmácia", "hospital", "mercado", "restaurante"]
    for local in locais:
        if local in comando:
            falar(f"Abrindo pesquisa para {local} próximo")
            webbrowser.open(f"https://www.google.com/maps/search/{local}")
            return
    
    falar("Desculpe, não entendi o comando.")

if __name__ == "__main__":
    while True:
        try:
            escolha = int(input("Digite:\n1 - Transformar texto em áudio\n2 - Transformar áudio em texto\n3 - Pesquisar por áudio\n999 - Finalizar o assistente\nEscolha: "))
        except ValueError:
            print("Entrada inválida! Digite um número válido.")
            continue
        
        if escolha == 1:
            texto = input("Digite o texto que deseja ouvir: ")
            falar(texto)
        elif escolha == 2:
            print("Fale algo para converter em texto...")
            texto = ouvir_comando()
            print("Texto reconhecido:", texto)
        elif escolha == 3:
            falar("Ouvindo seu comando...")
            comando = ouvir_comando()
            executar_comando(comando)
        elif escolha == 999:
            falar("Encerrando o assistente. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        time.sleep(1)