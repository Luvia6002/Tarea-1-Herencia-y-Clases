from Student import Student
from Secretary import Secretary
from Teacher import Teacher

student = Student("Sofia Vasquez", 20146785, "estudiante", "Lunes a Viernes", "S-12")
print("  ")
student.ingreso()
print(student)
student.entregarTarea()
print("  ")
student.salida()
print("------------------------")

secretary = Secretary("Maria Perez", 20105673, "secretaria", "Lunes a Domingo", "Departamento de matemática")
print("  ")
secretary.ingreso()
print(secretary)
secretary.hacerInforme()
print("  ")
secretary.salida()
print("-----------------------")

teacher = Teacher("Luis Galvez", 20215490, "maestro", "Martes y Juves", "T3")
print("  ")
teacher.ingreso()
print(teacher)
teacher.darClase()
print("  ")
teacher.salida()
print("-----------------------")
