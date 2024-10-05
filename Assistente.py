##Assistente:##
#Biblioteca:#
import os
from gtts import gTTS
import google.generativeai as genai

#Variáveis:#
NDU = ""  # Nome do usuário
NDA = ""  # Nome do assistente
SDA = ""  # Sexo do assistente
PAV = ""  # Preferência de atendimento com Voz
TPD = ""  # Texto pré-definido

PIA = ""  # Pergunta para IA
RIA = ""  # Resposta para IA

#Funções:#
def PPIA(PIA):  # função pergunta para IA
    global RIA
    try:
        genai.configure(api_key="SUA_CHAVE_DE_API")
        response = genai.generate_text(TPD + PIA)
        RIA = response['candidates'][0]['text'] if response else "Desculpe, não consegui entender sua pergunta."
        print(f"{NDA}: {RIA}")
    except Exception as e:
        print(f"Erro ao se comunicar com a IA: {e}")

def Audio(texto, nome_arquivo="resposta.mp3"):
    try:
        # Configurar a voz de acordo com o sexo do assistente
        if SDA == "H":
            tts = gTTS(text=texto, lang='pt', tld='com.br')  # TLD brasileiro para voz masculina
        else:
            tts = gTTS(text=texto, lang='pt')  # Voz feminina padrão
        
        # Criar o arquivo de áudio
        tts.save(nome_arquivo)
        print(f"Áudio criado: {nome_arquivo}")
        
        # Reproduzir o arquivo de áudio
        if os.path.exists(nome_arquivo):
            print(f"Reproduzindo: {nome_arquivo}")
            os.system(f"start {nome_arquivo}")  # Windows
            # Para Linux: os.system(f"mpg321 {nome_arquivo}")
            # Para Mac: os.system(f"afplay {nome_arquivo}")
        
        # Excluir o arquivo de áudio após a reprodução
        if os.path.exists(nome_arquivo):
            os.remove(nome_arquivo)
            print(f"Arquivo {nome_arquivo} excluído após a reprodução.")
    
    except Exception as e:
        print(f"Erro no processo de áudio: {e}")

#Comando:#
# Configuração:
print("Olá, usuário! Qual é o seu nome?")
NDU = input()

# Validação para o sexo do assistente
while True:
    print("Você prefere ser atendido por um homem ou uma mulher? (H/M)")
    SDA = input().upper()
    if SDA in ["H", "M"]:
        break
    print("Entrada inválida. Digite 'H' para Homem ou 'M' para Mulher.")

print("Qual nome você vai querer me chamar?")
NDA = input()

# Validação para a preferência de voz
while True:
    print("Vai querer que eu fale por áudio? (S/N)")
    PAV = input().upper()
    if PAV in ["S", "N"]:
        break
    print("Entrada inválida. Digite 'S' para Sim ou 'N' para Não.")

TPD = f"Olá, sou {NDA}, vou te chamar de {NDU}."

print("Muito bem, vamos continuar...")

# Uso normal:
if PAV == "S":
    while True:
        print(f"Certo {NDU}, qual vai ser sua pergunta?")
        PIA = input()
        PPIA(PIA)
        Audio(RIA)  # Responder com áudio
else:
    while True:
        print(f"Certo {NDU}, qual vai ser sua pergunta?")
        PIA = input()
        PPIA(PIA)  # Responder apenas em texto

#Fim:#
input()
