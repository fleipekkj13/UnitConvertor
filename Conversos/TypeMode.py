import sys
sys.path.insert(1,'./Conversos/')
from Conversos.Celsius import Celsius
from Conversos.Kelvin import Kelvin
from Conversos.Fahrenheit import Fahrenheit 
class TypeMode:
    def conversor(self,value,valueType,typeMode):

        self.valueType = valueType
        self.typeMode = typeMode
        self.value = value

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