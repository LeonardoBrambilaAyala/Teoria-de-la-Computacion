#include <iostream>
#include <set>
#define MaxDim 100

using namespace std;

class AFND
{
    private:
        set<int> Q; // Conjunto de estados
        set<char> Sigma; // Conjunto de simbolos de entrada
        int q0; // Estado inicial
        set<int> F; // Conjunto de estados de aceptacion
        set<pair<int, char>> delta[MaxDim]; // Funcion de transicion

    public:
        AFND(set<int> estados, set<char> simbolos, int estInicial, set<int> estAceptacion, set<pair<int, char>> transiciones[])
        {
            Q = estados;
            Sigma = simbolos;
            q0 = estInicial;
            F = estAceptacion;
            for(int i = 0; i < MaxDim; ++i) delta[i] = transiciones[i];
        }

        bool accept(string cadena)
        {
            set<int> estadoActuales;
            estadoActuales.insert(q0);

            //funcion de transicion extendida
            for(char w : cadena)
            {
                set<int> siguienteEstado;
                for (int estado : estadoActuales)
                {
                    //transiciones instantaneas
                    for(auto transicion : delta[estado])
                    {
                        if(transicion.second == '\0') //transicion instant�nea
                        {
                            siguienteEstado.insert(transicion.first);
                        }
                    }

                    // Transiciones normales
                    for(auto transicion : delta[estado])
                    {
                        if(transicion.second == w) // Transici�n normal
                        {
                            siguienteEstado.insert(transicion.first);
                        }
                    }
                }
                estadoActuales = siguienteEstado;
            }
            for(int estadoaux : estadoActuales)
            {
                if (F.find(estadoaux) != F.end())
                    return true;
            }

            return false;
        }
};

int main()
{
    set<int> estados = {0, 1, 2};
    set<char> simbolos = {'a', 'b'}; // Sigma
    int estInicial = 0; // Estado inicial
    set<int> estAceptacion = {2}; // Estado de aceptaci�n
    set<pair<int, char>> transiciones[MaxDim];

    // Definici�n de transiciones
    transiciones[0].insert({1, '\0'}); // Transici�n instant�nea de 0 a 1
    transiciones[1].insert({1, 'a'}); // Transici�n de 1 a 1 con 'a'
    transiciones[1].insert({2, 'b'}); // Transici�n de 1 a 2 con 'b'

    // Creaci�n del objeto AFND
    AFND afnd(estados, simbolos, estInicial, estAceptacion, transiciones);

    // Verificaci�n de cadenas de entrada
    string w;
    cout << "Ingrese una cadena para verificar si es aceptada por el AFND: ";
    cin >> w;

    if (afnd.accept(w))
        cout << "La cadena es aceptada por el AFND." << endl;
    else
        cout << "La cadena no es aceptada por el AFND." << endl;

    return 0;
}






