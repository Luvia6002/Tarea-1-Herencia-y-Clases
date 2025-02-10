from Person import Person

class Teacher(Person):
    def __init__(self, paramName: str, paramTarjet: int, paramWork: str, paramAvailableOn: str, ParamPlace: str):
        super().__init__(paramName, paramTarjet, paramWork, paramAvailableOn, ParamPlace)
    def darClase(self):
        print("Dando la clase")