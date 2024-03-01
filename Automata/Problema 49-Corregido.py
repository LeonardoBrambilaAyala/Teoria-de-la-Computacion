class AFND:
    def __init__(self, estados, simbolos, estInicial, estAceptacion, transiciones):
        self.Q = estados  #onjunto de estados
        self.Sigma = simbolos  #conjunto de simbolos de entrada
        self.q0 = estInicial  #estado inicial
        self.F = estAceptacion  #conjunto de estados de aceptacioon
        # self.delta = {}  #funcionn de tansicion extendida
        self.delta = transiciones

    def transicion(self, estado, simbolo):
        #devuelve el conjunto de estados alcanzables
        return self.delta.get(estado, {}).get(simbolo, set())
    #clausaura vacia
    def clausura_epsilon(self, estados):
        #clausura epsilon de un conjunto de estados
        clausura = set(estados)
        aux_Estados = list(estados)
        while aux_Estados:
            estado = aux_Estados.pop()
            for siguiente_estado in self.transicion(estado, ''):
                if siguiente_estado not in clausura:
                    clausura.add(siguiente_estado)
                    aux_Estados.append(siguiente_estado)
        return clausura

    def Estado_Aceptado(self, estados):
        #return estado in self.F
        #return any(estado in self.transicion(estado, ''))
        return any(estado in self.F for estado in estados)

    def Aceptado(self, cadena):
        #busqueda en profuncidad
        def dfs(estados, cadena):
            if cadena == "":
                return self.Estado_Aceptado(estados)
                #return any(self.es_estado_aceptacion(est) for est in self.clausura_epsilon(estados))
            else:
                primer_simbolo, resto_cadena = cadena[0], cadena[1:]
                nuevos_estados = set()
                for estado in estados:
                    #if '' in self.delta.get(estado_actual, {}):  #transiciones epsilon
                    #actualiza el conunto de estados a estados alcanzables
                    nuevos_estados.update(self.transicion(estado, primer_simbolo))
                return dfs(self.clausura_epsilon(nuevos_estados), resto_cadena)
        #el estado inicial, primero con trabsicion instantanea
        estados_iniciales = self.clausura_epsilon({self.q0})
        return dfs(estados_iniciales, cadena)

#main()
estados = {0, 1, 2}
simbolos = {'a', 'b'}
est_q0 = 0
est_A = {2}
transiciones = {
    0: {'': {1}},  # Transición epsilon de 0 a 1
    1: {'a': {1}, 'b': {2}},  # Transiciones con 'a' y 'b'
}

afnd = AFND(estados, simbolos, est_q0, est_A, transiciones)

cadena = input("Ingrese una cadena para verificar si es aceptada por el AFND: ")
if afnd.Aceptado(cadena):
    print("La cadena es aceptada por el AFND.")
else:
    print("La cadena no es aceptada por el AFND.")

