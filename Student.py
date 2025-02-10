from Person import Person

class Student(Person): 
    def __init__(self, paramName: str, paramTarjet: int, paramWork: str, paramAvailableOn : str, paramPlace: str):
        super().__init__(paramName, paramTarjet, paramWork, paramAvailableOn, paramPlace)

    def entregarTarea(self):
        print("Entregando la tarea")