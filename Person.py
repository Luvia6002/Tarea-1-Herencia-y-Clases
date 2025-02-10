class Person: 

    def __init__(self, paramName: str, paramTarjet: int , paramWork: str , paramAvailableOn: str , paramPlace: str):
        self.name = paramName
        self.tarjet = paramTarjet
        self.work = paramWork
        self.availableon = paramAvailableOn
        self.place = paramPlace

    def ingreso(self):
            print(f"La persona {self.name} ha llegado al la U") 

    def salida(self):
        print(f"La persona {self.name} ha salido de la U")

    def __str__(self):
            return f"""
            La persona {self.name} tiene carne {self.tarjet} es {self.work},
            de {self.availableon} en el {self.place}
            """