#funcion que calcula las personas contagiadas de la cepa Reino Unido
#la velocidad de contagio de la cepa del Reino Unido es el doble más cuatro personas que la cepa original,
def calcular_cepa_reino_unido(personas_contagiadas):
    return (personas_contagiadas * 2) + 4
#función que calcula las personas contagiadas de la cepa Brasileña
#la velocidad de contagio de la cepa brasileña está dada como la quinta parte de la suma de contagios de las otras dos versiones del virus
def calcular_cepa_brasil(personas_contagiadas_original, personas_contagiadas_reino_unido):
    return int((personas_contagiadas_original + personas_contagiadas_reino_unido)/5)
#función que determina el nivel de alerta
def calcular_nivel_alerta(personas_contagiadas):
    nivel_alerta = ""
    if (personas_contagiadas >= 0 and personas_contagiadas <= 20):
        nivel_alerta = "uno"
    elif (personas_contagiadas > 20 and personas_contagiadas <= 30):
        nivel_alerta = "dos"
    elif (personas_contagiadas > 30 and personas_contagiadas <= 50):
        nivel_alerta = "tres"
    elif (personas_contagiadas > 50):
        nivel_alerta = "cuatro"
    else:
        nivel_alerta = "No existe"
    return nivel_alerta
#Función main
def main():
    personas_contagiadas = int(input("Ingrese la cantidad de personas contagiadas: "))
    if (personas_contagiadas > 0):
        print(str(personas_contagiadas)+" "+str(calcular_cepa_reino_unido(personas_contagiadas))+" "+str(calcular_cepa_brasil(personas_contagiadas, calcular_cepa_reino_unido(personas_contagiadas))))
        print(calcular_nivel_alerta(calcular_cepa_brasil(personas_contagiadas, calcular_cepa_reino_unido(personas_contagiadas))))
    else:
        print("Por favor ingrese valores correctos (personas_contagiadas > 0)")

main()
