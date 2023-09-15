import sys
import os
from time import sleep
sys.path.insert(1,'./Conversos/')
from Conversos.TypeMode import TypeMode
from Conversos.textfile import printed

osSystem = None
if sys.platform.startswith("linux"):
        osSystem = "linux"
        def clearChat():
            os.system("clear")
else:
    osSystem = "Windows"
    def clearChat():
        os.system("cls")
class ConversorPt:
    def __init__(self):
        print("SE VOCÊ ENVIAR QUALQUER OUTRO VALOR QUE NÃO SEJA NÚMERO, VOCÊ ESTARA SAINDO DO CONVERSOR!")
        try:
            self.value = int(input("Insira apenas o valor de conversão:"))
            self.valueType = str(input("Qual escala é o seu valor? (C / F / K)")).capitalize()
            self.typeMode = str(input("Você deseja converter para qual tipo? (C / F / K)")).capitalize()

            TypeMode().conversor(self.value,self.valueType,self.typeMode)
        
        except:
            self.quitType = input("Você tem certeza que deseja sair?: (s/n) ").lower()
            if(self.quitType ==  "s"):
                return print("OK, até mais:) Obrigado por jogar!")
            else:
                print("Porfavor Aguarde!")
                sleep(2)
                os.system("cls")
                return ConversorPt()

class ConversorEn:
    def __init__(self):
        printed()
        print("IF YOU SEND ANY VALUE OTHER THAN NUMBERS, YOU QUIT THE APP!")
        try:
            self.value = int(input("Only type the value you want to Convert:"))
            clearChat()
            printed()
            self.valueType = str(input("What is your type value? (C / F / K)")).capitalize()
            clearChat()
            printed()
            self.typeMode = str(input("You want to convert for what type? (C / F / K)")).capitalize()
            clearChat()
            printed()
            TypeMode().conversor(self.value,self.valueType,self.typeMode)
        
        except:
            clearChat()
            printed()
            self.quitType = input("ARE YOU SURE YOU WANT TO QUIT?: (y/n) ").lower()
            if(self.quitType ==  "s"):
                clearChat()
                printed()
                return print("Alrigth, see you late :). Tnks for playing!")
            else:
                clearChat()
                printed()
                print("Please wait...")
                sleep(2)
                os.system("cls")
                return ConversorEn()

class ChooseTheLang:
    printed()
    def start():
        print("Por favor escolha a linguagem:\nPlease Select The Language: ")
        print("\n")
        try:
            lang = str(input("EN / PT : "))

            if(lang == "EN"):
                print("Starting the conversor in 'English' main language")
                clearChat()
                ConversorEn()

            else:
                print("Iniciando o conversor no idioma principal 'Português'")
                clearChat()
                ConversorPt()
        except:
            print("Idioma incorreto, por favor selecione entre 'pt' ou 'en'\nWrong language, please choose between 'pt' or 'en'")
            clearChat()
            ChooseTheLang()
            
    start()
ChooseTheLang()