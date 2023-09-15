'''
Formula Types:

K -> C: C = K - 273;
K -> F: (K-273) * 1,8 + 32;
C -> K: K = C + 273;
C -> F: F = C * 1,8 + 32;
F -> C: F = (F-32) / 1,8;
F -> K: K = (F-32) * 5/9 + 273;

'''

import os
from time import sleep

class Kelvin:
    def kelvinCel(value):
        result = value - 273
        return print(result)
    def kelvinFah(value):
        result = (value - 273) * 1.8 + 32
        return print(result)

class Celsius:
    def celKel(value):
        result = value + 273
        return print(result)
    def celFah(value):
        result = value * 1.8 + 32     
        return print(result)

class Fahrenheit:
    def fahCel(value):
        result = (value - 32) / 1.8
        return print(result)
    def fahKel(value):
        result = (value - 32) * 5/9 + 273
        return print(result)

class Conversor:
    def __init__(self):
        print("IF YOU SEND ANY VALUE OTHER THAN NUMBERS, YOU QUIT THE APP!")
        try:
            self.value = int(input("Only type the value you want to Convert:"))
            self.valueType = str(input("What is your type value? (C / F / K)")).capitalize()
            self.typeMode = str(input("You want to convert for what type? (C / F / K)")).capitalize()

            
            if(self.valueType == "C" and self.typeMode == "C"):
                return print(self.value)
            elif(self.valueType == "C" and self.typeMode == "F"):
                Celsius.celFah(self.value)
            elif(self.valueType == "C" and self.typeMode == "K"):
                Celsius.celKel(self.value)

            elif(self.valueType == "F" and self.typeMode == "F"):
                return print(self.value)
            elif(self.valueType == "F" and self.typeMode == "C"):
                Fahrenheit.fahCel(self.value)
            elif(self.valueType == "F" and self.typeMode == "K"):
                Fahrenheit.fahKel(self.value)
            
            elif(self.valueType == "K" and self.typeMode == "K"):
                return print(self.value)
            elif(self.valueType == "K" and self.typeMode == "C"):
                Kelvin.kelvinCel(self.value)
            elif(self.valueType == "K" and self.typeMode == "F"):
                Kelvin.kelvinFah(self.value)
        
        except:
            self.quitType = input("ARE YOU SURE YOU WANT TO QUIT?: (y/n) ").lower()
            if(self.quitType ==  "s"):
                return print("Alrigth, see you late :). Tnks for playing!")
            else:
                print("Please wait...")
                sleep(2)
                os.system("cls")
                return Conversor()

Conversor()