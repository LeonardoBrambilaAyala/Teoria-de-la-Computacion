def Automata_Finito_Determinista(cadena_Deseada):
    #crear los estados
    estados = [i for i in range(len(cadena_Deseada) + 1)]
    #estado_no_aceptado = len(cadena_Deseada)

    #transiciones
    transiciones = {}
    for i, caracteres in enumerate(cadena_Deseada):
        transiciones[(i, caracteres)] = i + 1

    #estado de aceptacion
    # Añadir transiciones al estado de no aceptación
    #for caracter in set(cadena_Deseada):
        #transiciones[(estado_no_aceptado, caracter)] = estado_no_aceptado

    #return estados, transiciones, estado_no_aceptado
    estado_De_Aceptacion = len(cadena_Deseada)

    return estados, transiciones, estado_De_Aceptacion

def acepta_cadena(afd, cadena):
    estados, transiciones, estado_De_Aceptacion = afd

    #estado actual
    actual = 0
    #i es igual a un caracter
    for i in cadena:
        actual = transiciones.get((actual, i), None)
        if actual is None:
            return False

    return actual == estado_De_Aceptacion

print("Programa de un automata finito determinista, para cualquier cadena\n")
cadena_Deseada = input("Teclea la cadena que desee: ")
afd = Automata_Finito_Determinista(cadena_Deseada)

cadena_Verificar = input("Teclee la cadena a verificar: ")
if acepta_cadena(afd, cadena_Verificar):
    print("Cadena aceptada.")
else:
    print("Cadena no aceptada.")

print("\nSe buscan las subcadenas de: ", cadena_Deseada, "\n")
if cadena_Verificar in cadena_Deseada:
    print("Subcadena aceptada.")
else:
    print("Subcadena no aceptada.")