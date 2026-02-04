#Importamos el sistema para que funcione algo que no me dejan poner porque es trampa UwU
import sys

# No se para que sirve los primeros parametros
# Tipos de monstruo
NO_MUERTO = 1
BESTIA = 2
DEMONIO = 3
HUMANOIDE = 4
ELEMENTAL = 5

# Hábitats
BOSQUE = 1
MAZMORRA = 2
DESIERTO = 3
MONTANYA = 4
PANTANO = 5

# Modos de ataque
CUERPO_A_CUERPO = 1
MAGIA = 2
A_DISTANCIA = 3

# Tamaños
PEQUENO = 1
MEDIANO = 2
GRANDE = 3
ENORME = 4

# Rangos de atributos
NIVEL_MIN = 1
NIVEL_MAX = 100

VELOCIDAD_MIN = 1
VELOCIDAD_MAX = 10

#Función leer ficheros
def leer_datos (lista_nombre : list , lista_tipo : list , lista_nivel : list , lista_habitat : list , lista_ataque : list , lista_tamanyo : list ,lista_velocidad : list ,) -> bool :
    fichero = None
    try:
        fichero = open('./Mounstruos.txt', 'r')
        #guardamos todos los valores donde corresponde
        for linea in fichero:
            valores = linea.split()
            lista_nombre.append(valores[0])
            lista_tipo.append(int(valores[1]))
            lista_nivel.append(int(valores[2]))
            lista_habitat.append(int(valores[3]))
            lista_ataque.append(int(valores[4]))
            lista_tamanyo.append(int(valores[5]))
            lista_velocidad.append(int(valores[6]))
    # Encontramos el error de que no hay fichero
    except FileNotFoundError:
        return False
    except:
        return False
    # Cerramos el fichero
    finally:
        if fichero != None:
            fichero.close()
    return True

#Función para crear el menu
def menu() -> int:
    while True:
        try:
            print("\n")
            print("-"*19, "Menú de opciones", "-"*19)
            print("1. Mostrar mounstruos por tipo, hábitat y modo de ataque")
            print("2. Listar mountruos muy peligrosos y poco peligrosos")
            print("3. Mostrar porcentaje de uso de modos de ataque")
            print("4. Agrupar a mounstruos por hábitat")
            print("0. Salir.")
            print("-"*57)
            opcion = int(input("Elige una opción: "))
            if opcion <= 4 and opcion >= 0:
                return opcion
            else:
                print("Error: Elige una de las opciones mostradas\n")
        except Exception as e:  
            print("Error:", e)

# Función mostrar monstruos
def mostrar_monstruos ( lista_nombre : list , lista_tipo : list , lista_nivel : list , lista_habitat : list , lista_ataque : list , lista_velocidad : list, tipo: int, habitat: int, modo_ataque: int) -> None :
    mostrar_nombre = []
    mostrar_nivel = []
    mostrar_velocidad = []
    #Recorremos las listas
    for a in range (len(lista_tipo)):
        if tipo == lista_tipo[a]:
            if habitat == lista_habitat[a]:
                if modo_ataque == lista_ataque[a]:
                    mostrar_nombre.append(lista_nombre[a])
                    mostrar_nivel.append(lista_nivel[a])
                    mostrar_velocidad.append(lista_velocidad[a])
    # Si no existe el monstruo vaya pringado que eres bobo
    if len(mostrar_nombre) == 0:
        print("No se han encontrado monstruos")
    # Has encontrado el monstruo
    else:
        print("\nMonstruos encontrados:")
        for x in range(len(mostrar_nombre)):
            print(f'-{mostrar_nombre[x]}', end = "\t")
            print(f'Nivel: {mostrar_nivel[x]}', end = "\t")
            print(f'Velocidad:{mostrar_velocidad[x]}')


# Función meter monstruos en un fichero
def generar_fichero_peligrosos(lista_nombre: list, lista_nivel: list, umbral_alto: int = 80, umbral_bajo: int = 20) -> bool:
    fichero_muy_peligrosos = None
    fichero_poco_peligrosos = None
    try:
        fichero_poco_peligrosos = open('./monstruos_poco_peligrosos.txt', 'w')
        fichero_muy_peligrosos = open('./monstruos_muy_peligrosos.txt', 'w')
        lista_alto = []
        lista_bajo = []
        # Guardamos monstruos en la lista según los parametros dados
        for x in range(len(lista_nombre)):
            if lista_nivel[x] >= umbral_alto:
                lista_alto.append(lista_nombre[x])
            elif lista_nivel[x] <= umbral_bajo:
                lista_bajo.append(lista_nombre[x])
        # Guardamos monstruos petitis :( que bonito y los mayores se guardan solos :)
        for petits in lista_bajo:
            fichero_poco_peligrosos.write(f'{petits} \n')
        for mayorcitos in lista_alto:
            fichero_muy_peligrosos.write(f'{mayorcitos} \n')
    except FileNotFoundError:
        print("Error: El fichero no existe")
        sys.exit(1)
    except Exception as e:
        print("Error:", e)
        sys.exit(1)
    # Te cierro el culo
    finally:
        if fichero_muy_peligrosos != None:
            fichero_muy_peligrosos.close()
        if fichero_poco_peligrosos != None:
            fichero_poco_peligrosos.close()
    
    #Esta parte de la función lo hago porque me apetece no me lo borres porfi pls que lo necesito para ver si se ha guardado correctamente
    '''
    #Leer fichero
    fichero_poco_peligrosos = None
    fichero_muy_peligrosos = None
    try:
        fichero_poco_peligrosos = open('./monstruos_poco_peligrosos.txt', 'r')
        fichero_muy_peligrosos = open('./monstruos_muy_peligrosos.txt', 'r')
        print("Monstruos poco peligrosos:")
        for monstruos_peques in fichero_poco_peligrosos:
            monstruos_peques = monstruos_peques.strip().split()
            print(monstruos_peques)
        print("Monstruos muy peligrosos:")
        for monstruos_grandes in fichero_muy_peligrosos:
            monstruos_grandes = monstruos_grandes.strip().split()
            print(monstruos_grandes)
    except FileNotFoundError:
        print("Error: Fichero no encontrado")
        sys.exit(1)
    except Exception as e:
        print("Error:", e)
        sys.exit(1)
    finally:
        if fichero_muy_peligrosos != None:
            fichero_muy_peligrosos.close()
        if fichero_poco_peligrosos != None:
            fichero_poco_peligrosos.close()
    '''

# Función mostrar porcentaje de ataques
def mostrar_porcentaje_uso_modos(lista_ataque: list) -> None:
    modo_cuerpo = 0
    modo_magia = 0
    modo_distancia = 0
    # Mirar que modo de ataque es
    for modo in lista_ataque:
        if modo == CUERPO_A_CUERPO:
            modo_cuerpo += 1
        elif modo == MAGIA:
            modo_magia += 1
        elif modo == A_DISTANCIA:
            modo_distancia += 1
    #Calcular el porcentaje de amor por ella. PD: Ninguno :(
    porcentaje_cuerpo = (modo_cuerpo/len(lista_ataque))*100
    porcentaje_magia = (modo_magia/len(lista_ataque))*100
    porcentaje_distancia = (modo_distancia/len(lista_ataque))*100
    #Printeando por la vida
    print("-"*3, "Porcentaje de uso de modos de ataque", "-"*3, "\n")
    print(f'Modo 1 (Cuerpo a cuerpo): {porcentaje_cuerpo:.2f}%')
    print(f'Modo 2 (Magia): {porcentaje_magia:.2f}%')
    print(f'Modo 3 (A distancia): {porcentaje_distancia:.2f}%')

# Función agrupar monstruo en su habitat
def agrupar_por_habitat (lista_nombre : list , lista_nivel : list , lista_habitat : list, habitat : int) -> tuple [list , list ]:
    nombre = []
    nivel = []
    # Lo mismo de simepre, ya lo sabes. Y sino aprende que ya vas tarde bobo
    for monstruos in range(len(lista_habitat)):
        if lista_habitat[monstruos] == habitat:
            nombre.append(lista_nombre[monstruos])
            nivel.append(lista_nivel[monstruos])
                    
    print(f'Monstruos en el habitat {habitat}:')
    for monstruo in nombre:
        print(f'-{monstruo}')
    print(f'Niveles encontrados: {nivel}')

# Función main
def main() -> None:
    # Todas las listas necesarias (o eso creo)
    lista_nombre = []
    lista_tipo = []
    lista_nivel = []
    lista_habitat = []
    lista_ataque = []
    lista_tamanyo = []
    lista_velocidad = []
    # Llamamos a la función para conseguir los datos de los monstruos
    valor = leer_datos(lista_nombre, lista_tipo, lista_nivel, lista_habitat, lista_ataque, lista_tamanyo, lista_velocidad)
    print(f'¿Se ha leído el fichero? {valor}')
    # Bucle Bucle Bucle Bucle Bucle Bucle Bucle Bucle Bucle Bucle Bucle Bucle Bucle Bucle Bucle Bucle Bucle Bucle Bucle Bucle Bucle Bucle Bucle 
    # '#chiste'
    while True:
        # Imprimimos menu
        opcion = menu()
        if opcion == 1:
            print("Tipo de Mountruo:\n 1: No-muerto\n 2: Bestia\n 3: Demonio\n 4: Humanoide\n 5: Elemental")
            while True:
                try:
                    tipo = int(input("Dime un tipo: "))
                    if tipo > 0 and tipo < 6:
                        break
                    else:
                        print("No existe este tipo de mounstruo")
                except Exception as e:
                    print("Error:", e)

            print("\n")
            print("Hábitat del mounstruo:\n 1: Bosque\n 2: Mazmorra\n 3: Desierto\n 4: Montaña\n 5: Pantano")
            while True:
                try:
                    habitat = int(input("Dime un habitat: "))
                    if habitat > 0 and habitat < 6:
                        break
                    else:
                        print("No existe este tipo de hábitat")
                except Exception as e:
                    print("Error:", e)

            print("\n")
            print("Modo de ataque del mounstruo:\n 1: Cuerpo a Cuerpo\n 2: Magia\n 3: A distancia")
            while True:
                try:
                    modo_ataque = int(input("Dime el tipo de ataque: "))
                    if modo_ataque > 0 and modo_ataque < 4:
                        break
                    else:
                        print("No existe este tipo de ataque")
                except Exception as e:
                    print("Error", e)
            mostrar_monstruos(lista_nombre, lista_tipo, lista_nivel, lista_habitat, lista_ataque, lista_velocidad, tipo, habitat, modo_ataque)
        elif opcion == 2:
            while True:
                try:
                    defecto = input("¿Quieres usar los valores por defecto (Si o No)? ").lower()
                    if defecto == "si":
                        generar_fichero_peligrosos(lista_nombre, lista_nivel)
                        break           
                    elif defecto == "no":
                        umbral_bajo = int(input("Elige el nivel bajo de peligrosidad (0-100): "))
                        umbral_alto = int(input("Elige el nivel alto de peligrosidad (0-100): "))
                        if umbral_bajo > umbral_alto:
                            print("Error: Nivel incorrecto")
                        elif umbral_alto <= 0 or umbral_alto >= 100 or umbral_bajo <= 0 or umbral_bajo >= 100:
                            print("Error: Nivel incorrecto")
                        else:
                            generar_fichero_peligrosos(lista_nombre, lista_nivel, umbral_alto, umbral_bajo)
                            break
                    else:
                        print("Error: Opción incorrecta")
                except Exception as e:
                    print("Error:", e)
                    sys.exit(1)
        elif opcion == 3:
            mostrar_porcentaje_uso_modos(lista_ataque)            
        elif opcion == 4:
            while True:
                try:
                    print("Habitats:\n 1. Bosque\n 2. Mazmorra\n 3. Desierto\n 4. Montaña\n 5. Pantano")
                    habitat = int(input("¿Qué monstruos quieres saber donde están? "))
                    if habitat > 0 and habitat < 6:
                        break
                    else:
                        print("Error: Opción elegida incorrecta")
                except Exception as e:
                    print("Error:", e)
            agrupar_por_habitat(lista_nombre, lista_nivel, lista_habitat, habitat)
        elif opcion == 0:
            print("Saliendo...")
            sys.exit(1)
        else:
            print("Error: Opción elegida no exite")

if __name__ == "__main__":
    main()

# Todo lo que digo en las anotaciones es para mi para acordarme y motivarme, "QUE NADIE SE SIENTA ALUDIDO, (bobo)"