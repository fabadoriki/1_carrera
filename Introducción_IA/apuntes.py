'''
La inteligencia artificial simbólica es una rama fundamental de la IA que representa el conocimiento mediante símbolos y lógica formal. A diferencia de
otros enfoques, esta metodología estructura el razonamiento de manera explícita y comprensible.

CARACTERÍSTICAS CLAVES:
    - Conocimiento explícito: El razonamiento se puede seguir paso a paso, permitiendo una compresión total del proceso de tomas de decisiones+
    - Explicabilidad total: Cada conclusión puede ser justificada mostrando exactamente qué hechos y reglas se utilizaron, facilitaron la audiotiría 
        y validación del sistema
    - Inferencia lógica: Capacidad de descubrir conocimiento ímplcito a partir del explícito mediante razonamiento deductivo riguroso y sistemático
'''
'''
HECHOS:
Los hechos constituyen las afirmaciones básicas que el sistema considera verdaderas y verificables. Representan el conocimiento
fundamental sobre el mundo que alimenta todo el proceso de razonamiento
Estos se expresan como proposiciones simples y directas, sin ambigüedades, permitiendo que el sistema opere con certeza sobre
la información disponible

REGLAS:
Las reglas son el corazón del sistema de IA simbólica. Describen cómo se relacionan los hechos entre sí y permiten deducir nueva
información a partir del conocimiento existente
    - Estructura Condicional: Las reglas si el formato es lógico "si A entonces B", estableciendo relaciones causales claras
    - Aplicación de la Regla: Cuando se cumple la condición A, el sistema puede inferir automáticamente la conclusión B
    - Genereación de Conocimiento: El proceso permite descubrir información ímplicita que no está explícitame declarada

CARACATERISTICAS:
    - Conocimiento explicito: El razonamiento es completamente transparente y se puede seguir paso a paso (compresión total)
    - Explicabilidad total: Cada conclusión puede ser justificada mostrando exactamente qué hechos y reglas se utilizaron
    - Inferencia lógica: Capacidad de descubrir conocimiento implícito a partir del explicíto mediante el razonamiento deductivo y riguroso y sistemático

'''
'''
.clear() para quitar lo programado de anterioridad
.create_terms() -> Define los hecho y las reglas
hechos (+"hecho") -> Afirmaciones básicas
    · Simbolos (predicados): suele ir en minusculas
    · Átomos (cadenas o números): se escriben como 'texto' o 123
reglas (<=) -> Implicación lógica
consulta -> Pregunta al sistema
variables -> Suelen estar en mayusculas, hacen el proceso de unificación 
'''
'''
Como leer una regla:
    - Conclusión <= condición

Creación de bases de concimientos:
    - Primero tenemos que generar una base de concimientos donde declaramos todos los hechos
        from pyDatalog import pyDatalog
        pyDatalog.clear()
        pyDatalog.create_terms('permiso,rol')
        +permiso('admin','leer')
        +permiso('admin','escribir')
        +permiso('admin','borrar')
        +rol('Marta','editor')
        +rol('Eloina','admin')

Reglas de inferecia lógica:
    - Las reglas permiten deducir nueva información a partir de los hechos conocidos 
    tiene_permiso(U, P) <= rol(U,R) & permiso(R,P)

Negación -> (~)
'''