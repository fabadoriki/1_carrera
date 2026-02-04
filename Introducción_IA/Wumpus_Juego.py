#Importamos la biblioteca "pyDatalog"
from pyDatalog import pyDatalog
pyDatalog.clear()
#Indicamos todos los terminos que necesitamos para el programa
pyDatalog.create_terms('numero', 'brisa', 'hedor', 'hoyo', 'ady', 'tablero', 'segura', 'brillo', 'wumpus', 'tesoro',)
pyDatalog.create_terms('posible_hoyo', 'posible_wumpus', 'no_hoyo', 'no_wumpus', 'no_hedor', 'no_brisa')
pyDatalog.create_terms('X', 'Y', 'X1', 'X2', 'Y1', 'Y2')

#Los números que pueden tomar las coordenadas (1 al 4)
+numero(1); +numero(2); +numero(3); +numero(4);

#La regla de que el tablero coge los números de las coordenadas, para crear el tablero 
tablero(X, Y) <= numero(X) & numero(Y)

#Creamos la regla de adyaciencia para saber todas las adyaciencias en el tablero
ady(X1, Y1, X2, Y2) <= tablero(X1, Y1) & tablero(X2, Y2) & (X2 == X1+1) & (Y2 == Y1)
ady(X1, Y1, X2, Y2) <= tablero(X1, Y1) & tablero(X2, Y2) & (X2 == X1-1) & (Y2 == Y1)
ady(X1, Y1, X2, Y2) <= tablero(X1, Y1) & tablero(X2, Y2) & (X2 == X1) & (Y2 == Y1+1)
ady(X1, Y1, X2, Y2) <= tablero(X1, Y1) & tablero(X2, Y2) & (X2 == X1) & (Y2 == Y1-1)

#Casillas que sabemos que estamos seguros que no son "malas" como la brisa, el hedor y el brillo, las ponemos como un hecho
+brisa(2, 1)
+brisa(4, 1)
+brisa(3, 2)
+brisa(2, 3)
+brisa(4, 3)
+brisa(3, 4)
+hedor(1, 4)
+hedor(1, 2)
+hedor(2, 3)
+brillo(2, 3)

#Indicamos donde está el tesoro
tesoro(X,Y) <= brillo(X,Y)

#Creamos las reglas para definir que casillas seguras hay en el tablero
segura(X,Y) <= brisa(X,Y)
segura(X,Y) <= hedor(X,Y)
segura(X,Y) <= brillo(X,Y) 

#Creamos una regla para saber que en las casillas adyacentes donde no hay una brisa no puede haber un hoyo
no_hoyo(X,Y) <= tablero(X, Y) & ady(X, Y, X2, Y2) & ~brisa(X2,Y2)
#Vemos la posibilidad de que haya un hoyo, si encontramos una brisa
posible_hoyo(X, Y) <= tablero(X,Y) & ~no_hoyo(X,Y) & ~segura(X,Y)

#Creamos una regla paraber que en las casillas adyacentes donde no hay un hedor no puede estar wumpus
no_wumpus(X,Y) <= tablero(X,Y) & ady(X, Y, X2, Y2) & ~hedor(X2, Y2)
#Vemos que haya la posibilidad de que este el wumpus, si encontramos hedor
posible_wumpus(X, Y) <= tablero(X, Y) & ~no_wumpus(X, Y) & ~segura(X, Y)

#Aplicamos la última regla de casilla segura
segura(X,Y) <= no_hoyo(X,Y) & no_wumpus(X,Y)


#EMPEZAMOS EL PROGRAMA
def hacer_matriz():
    #Hacemos un tablero para que el aventurero sepa que casillas puedes asegurar
    tablero = [
        [4, "O", "O", "O", "O"],
        [3, "O", "O", "O", "O"],
        [2, "O", "O", "O", "O"],
        [1, "O", "O", "O", "O"],
        ["-", 1, 2, 3, 4]
    ]
    #Imprimimos el tablero
    for fila in tablero:
        for elementos in fila: 
            print(elementos, end = " ")
        print( )

def mirar_casilla(columna, fila):
    #Preguntamos todas las preguntas en las que podemos dar respuestas al aventurero 
    print(f'¿Es segura la casilla ({columna},{fila})?')
    if bool(segura(columna,fila)):
        print("SI")
    else:
        print("NO")
    print(f'\n ¿Se puede asegurar que no hay hoyo en la casilla ({columna},{fila})')
    if bool(no_hoyo(columna,fila)):
        print("SI")
    else:
        print("NO")
    print(f'\n¿Puede haber hoyo en la casilla ({columna},{fila})?')
    if bool(posible_hoyo(columna, fila)):
        print("SI")
    else:
        print("NO")
    print(f'\n¿Se puede asegurar que no hay wumpus en la casilla ({columna}, {fila})?')
    if bool(no_wumpus(columna,fila)):
        print("SI")
    else:
        print("NO")
    print(f'\n¿Puede haber wumpus en la casilla ({columna}, {fila})?')
    if bool(posible_wumpus(columna,fila)):
        print("SI")
    else:
        print("NO")
    print(f'\n¿Se puede asegurar que la casilla ({columna}, {fila})?')
    if bool(segura(columna,fila)):
        print("SI")
    else:
        print("NO")
#Empezamos el progama general
#Creamos un bucle para que el aventurero pueda preguntar por cualquier casilla, hasta que pare de jugar
while True:
    #Preguntamos si el aventurero quiere jugar al juego de Wumpus
    jugar = input("\n¿Quieres jugar (Si o No)? ").upper()
    if jugar == "SI":
        while True:
            #Imprimimos el tablero
            print("\n TABLERO:")
            hacer_matriz()
            print("\n")
            #Preguntamos la casilla que quiere averiguar
            columna = int(input("¿Que columna quieres mirar (1 al 4)? "))
            fila = int(input("¿Que fila quieres mirar (1 al 4)? "))
            #Si la casilla introducida no está dentro del tablero, se indica que no exite la casilla y se vuelve a preguntar la casilla 
            if columna > 0 and columna < 5 and fila > 0 and fila < 5:
                #Imprimimos la función que resuelve las preguntas del aventurero
                mirar_casilla(columna, fila)
                break
            else:
                print("Esta casilla no existe")
        if bool(tesoro(columna,fila)):
            print("\n¡HAS ENCONTRADO EL TESORO!")
            print("-"*5, "¡ENHORABUENA!", "-"*5)
            break
    elif jugar == "NO":
        print("El juego se ha acabado")
    else:
        print("Di entre Si o No")
