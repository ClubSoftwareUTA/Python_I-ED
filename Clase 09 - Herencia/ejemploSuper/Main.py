from Persona import Persona
from Empleado import Empleado

jose=Persona("Jose", 20, "Colombia")
jose.descripcion()

juan=Empleado(1500, 15, "Juan", 55, "España")
juan.descripcion()

print(isinstance(juan, Empleado))
print(isinstance(juan, Persona))
print(isinstance(jose, Empleado))