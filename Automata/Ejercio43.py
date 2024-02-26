
class AFND:
    def __init__(self, estados, simbolos, estInicial, estAceptacion, transiciones):
        self.Q = estados  #onjunto de estados
        self.Sigma = simbolos  #conjunto de simbolos de entrada
        self.q0 = estInicial  #estado inicial
        self.F = estAceptacion  #conjunto de estados de aceptación
        # self.delta = {}  #funcionn de tansicion extendida
        self.delta = transiciones

    def accept(self, cadena):
        def dfs(estadoActual, cadena):
            if cadena == "":
                #if estado_actual in self.F:
                    #return True
                return estadoActual in self.F
            for siguienteEstado in self.delta.get(estadoActual, {}).get('', []):
                if dfs(siguienteEstado, cadena):
                        return True
                    #return False
            primerSimbolo, restoCadena = cadena[0], cadena[1:]
            for siguienteEstado in self.delta.get(estadoActual, {}).get(primerSimbolo, []):
                if dfs(siguienteEstado, restoCadena):
                    return True
            return False
        #return dfs(cadena, self)
        return dfs(self.q0, cadena)
            #if estado_actual in self.delta and primer_simbolo in self.delta[estado_actual]:
             #   for siguiente_estado in self.delta[estado_actual][primer_simbolo]:
              #      if dfs(siguiente_estado, resto_cadena):
               #         return True
            #if '' in self.delta.get(estado_actual, {}):  #transiciones epsilon
             #   for siguiente_estado in self.delta[estado_actual]['']:
              #      if dfs(siguiente_estado, cadena):
               #         return True
            #return False

        #return dfs(self.q0, cadena)

#AFND para aceptar L*
estados = {0, 1, 2, 3, 4, 5}
simbolos = {'a', 'b', 'c', 'd'}
est_inicial = 0
est_aceptacion = {0}  # El estado inicial, podia ser tambien el de aceptacion para que esta valide la cadena vacia
transiciones = {
    0: {'': {1, 3}},  #transiciones ε para empezar a procesar "ab" o "cd"
    1: {'a': {2}},    #tansicion para "a" en {"ab"}
    2: {'b': {0}},    #transicion de vuelta al estado inicial despues de "b"
    3: {'c': {4}},    #transicion para "c" en {"cd"}
    4: {'d': {0}},    #transicion de vuelta al estado inicial despies de "d"
}

afnd = AFND(estados, simbolos, est_inicial, est_aceptacion, transiciones)

cadena = input("Ingrese una cadena para verificar si es aceptada por el AFND: ")
if afnd.accept(cadena):
    print("La cadena es aceptada por el AFND.")
else:
    print("La cadena no es aceptada por el AFND.")
