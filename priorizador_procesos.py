
# Reglas del puntaje de beneficio
MINUTOS_POR_HORA = 60
DECIMALES_HORAS = 1
HORAS_REFERENCIA = 200
PUNTOS_MAXIMOS_HORAS = 60
PUNTOS_MAXIMOS_REGLAS = 40
PORCENTAJE_MAXIMO = 100
DECIMALES_PUNTAJE = 1

# Reglas del puntaje de complejidad
PUNTOS_POR_APLICACION = 10
PUNTOS_ESTABILIDAD = {"baja": 40, "media": 20, "alta": 0}
COMPLEJIDAD_MAXIMA = 100

# Cortes de la matriz de clasificación
BENEFICIO_MINIMO_QUICK_WIN = 60
COMPLEJIDAD_MAXIMA_QUICK_WIN = 40
CLASIFICACION_QUICK_WIN = "Quick Win"
CLASIFICACION_CANDIDATO = "Candidato"
CLASIFICACION_DESCARTADO = "Descartado"

PROCESOS = [
    

{
    "nombre": "Conciliación bancaria",
    "transacciones_mes": 1200,
    "minutos_por_transaccion": 5,
    "cantidad_aplicaciones": 2,
    "porcentaje_reglas_claras": 80,
    "estabilidad": "alta",
},
{
    "nombre": "Facturación",
    "transacciones_mes": 3000,
    "minutos_por_transaccion": 6,
    "cantidad_aplicaciones": 5,
    "porcentaje_reglas_claras": 50,
    "estabilidad": "baja",

    },

{
        "nombre": "Registro de pedidos",
        "transacciones_mes": 2400,
        "minutos_por_transaccion": 6,
        "cantidad_aplicaciones": 3,
        "porcentaje_reglas_claras": 90,
        "estabilidad": "alta",
    },

{
        "nombre": "Atención de reclamos",
        "transacciones_mes": 300,
        "minutos_por_transaccion": 10,
        "cantidad_aplicaciones": 6,
        "porcentaje_reglas_claras": 30,
        "estabilidad": "baja",
    },

{
     "nombre": "Creación de usuarios",
        "transacciones_mes": 400,
        "minutos_por_transaccion": 3,
        "cantidad_aplicaciones": 1,
        "porcentaje_reglas_claras": 90,
        "estabilidad": "alta",
    },
{
        "nombre": "Cierre contable mensual",
        "transacciones_mes": 500,
        "minutos_por_transaccion": 12,
        "cantidad_aplicaciones": 8,
        "porcentaje_reglas_claras": 60,
        "estabilidad": "baja",
 },

{
        "nombre": "Envío de reportes",
        "transacciones_mes": 1000,
        "minutos_por_transaccion": 6,
        "cantidad_aplicaciones": 2,
        "porcentaje_reglas_claras": 75,
        "estabilidad": "media",
    },
{
        "nombre": "Actualización de inventario",
        "transacciones_mes": 250,
        "minutos_por_transaccion": 7,
        "cantidad_aplicaciones": 2,
        "porcentaje_reglas_claras": 70,
        "estabilidad": "media",
    },

]
def calcular_horas_ahorradas(transacciones_mes, minutos_por_transaccion):
    """Devuelve las horas que se ahorran al mes, con un decimal."""
    minutos_totales = transacciones_mes * minutos_por_transaccion
    horas = minutos_totales / MINUTOS_POR_HORA
    return round(horas, DECIMALES_HORAS)

def calcular_puntaje_beneficio(horas, porcentaje_reglas_claras):
    """Devuelve el puntaje de beneficio, de 0 a 100."""
    if horas > HORAS_REFERENCIA:
        horas_para_puntaje = HORAS_REFERENCIA
    else:
        horas_para_puntaje = horas
    puntos_horas = horas_para_puntaje / HORAS_REFERENCIA * PUNTOS_MAXIMOS_HORAS
    puntos_reglas = porcentaje_reglas_claras / PORCENTAJE_MAXIMO * PUNTOS_MAXIMOS_REGLAS
    return round(puntos_horas + puntos_reglas, DECIMALES_PUNTAJE)

def calcular_puntaje_complejidad(cantidad_aplicaciones, estabilidad):
    """Devuelve el puntaje de complejidad, de 0 a 100."""
    puntos_aplicaciones = cantidad_aplicaciones * PUNTOS_POR_APLICACION
    puntos_estabilidad = PUNTOS_ESTABILIDAD[estabilidad]
    complejidad = puntos_aplicaciones + puntos_estabilidad
    if complejidad > COMPLEJIDAD_MAXIMA:
        complejidad = COMPLEJIDAD_MAXIMA
    return complejidad

def clasificar_proceso(beneficio, complejidad):
    """Devuelve la clasificación del proceso según la matriz."""
    beneficio_alto = beneficio >= BENEFICIO_MINIMO_QUICK_WIN
    complejidad_baja = complejidad <= COMPLEJIDAD_MAXIMA_QUICK_WIN
    if beneficio_alto and complejidad_baja:
        return CLASIFICACION_QUICK_WIN
    elif not beneficio_alto and not complejidad_baja:
        return CLASIFICACION_DESCARTADO
    else:
        return CLASIFICACION_CANDIDATO


for proceso in PROCESOS:
    horas = calcular_horas_ahorradas(
        proceso["transacciones_mes"],
        proceso["minutos_por_transaccion"],
    )
    beneficio = calcular_puntaje_beneficio(
        horas,
        proceso["porcentaje_reglas_claras"],
    )
    complejidad = calcular_puntaje_complejidad(
        proceso["cantidad_aplicaciones"],
        proceso["estabilidad"],
    )
    clasificacion = clasificar_proceso(beneficio, complejidad)
    print(proceso["nombre"], horas, beneficio, complejidad, clasificacion)
