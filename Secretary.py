from Person import Person
class Secretary(Person):
    def __init__(self, paramName: str, paramTarjet: int, paramWork: str, paramAvailableOn: str, paramPlace: str):
        super().__init__(paramName, paramTarjet, paramWork, paramAvailableOn, paramPlace)

    def hacerInforme(self):
        print("Redactando un informe")