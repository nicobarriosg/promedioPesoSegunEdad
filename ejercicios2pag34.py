p = int(input("Ingrese el numero de personas para el muestreo: "))

niño = 0
joven = 0
adulto = 0
tercera_edad = 0

peso = 0
peso_niño = 0
peso_joven = 0
peso_adulto = 0
peso_tercera_edad = 0

for i in range(p):

    edad = int(input(f"Ingrese la EDAD de la {i+1} persona: "))
    peso = int(input(f"Ingrese el PESO de la {i+1} persona: "))

    if edad <= 12:
        niño += 1
        peso_niño += peso
    elif edad >= 13 and edad <= 29:
        joven += 1
        peso_joven += peso
    elif edad >= 30 and edad <= 59:
        adulto += 1
        peso_adulto += peso
    else:
        tercera_edad += 1
        peso_tercera_edad += peso

promedio_niño = int(peso_niño / niño if niño > 0 else 0)
promedio_joven = int(peso_joven / joven if joven > 0 else 0)
promedio_adulto = int(peso_adulto / adulto if adulto > 0 else 0)
promedio_tercera_edad = int(peso_tercera_edad / tercera_edad if tercera_edad > 0 else 0)


print(("El promedio de peso en niños es de {}").format(promedio_niño))
print(("El promedio de peso en jovenes es de {}").format(promedio_joven))
print(("El promedio de peso en adultos es de {}").format(promedio_adulto))
print(("El promedio de peso en personas de la tercera edad es de {}").format(promedio_tercera_edad))