#Assistente#
#Biblitecas:
import PySimpleGUI as sg
from gtts import gTTS
import google.generativeai as genai
#Variaveis:
sg.theme('DarkBrown1');
Layot = Layot1
LAR = 1200;#largura
ALT = 600;#altura


#Layot:
Layot1 = [
            [sg.text("Pré configuração:")],
            [sg.HorizontalSeparator()],
            [sg.text("Olá usuario! Qual é o seu nome?")], [sg.button("Voz")],
            [sg.Input()],
            [sg.text("Você prefere o ser atendido por um homem ou uma mulher?")], [sg.button("Voz")],
            [sg.button("Homem")], [sg.button("Mulher")],
            [sg.text("Qual nome você vai querer me chamar?")], [sg.button("Voz")],
            [sg.input()],
            [sg.HorizontalSeparator()],
            [sg.text("Muito bem vamos continuar..")], [sg.button("Voz")],
            [sg.button("Continuar")],
         ]

Layot2 = [
            [sg.text("Assistente:")],
            [sg.HorizontalSeparator()],
            [sg.text("O que você precisa? USUARIO")],
            [sg.input()],
            [sg.text("")],
         ]
#Configurações:
window = sg.window('Assistente', Layot);
#Comando:
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
#Fim:
window.close()