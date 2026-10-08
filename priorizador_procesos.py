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

# Presentación de la salida
ANCHO_NOMBRE = 30
ANCHO_COLUMNA = 13

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


def evaluar_proceso(proceso):
    """Devuelve un diccionario con los resultados de un proceso."""
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
    return {
        "nombre": proceso["nombre"],
        "horas": horas,
        "beneficio": beneficio,
        "complejidad": complejidad,
        "clasificacion": clasificacion,
    }


def evaluar_procesos(procesos):
    """Devuelve la lista de resultados de todos los procesos."""
    resultados = []
    for proceso in procesos:
        resultados.append(evaluar_proceso(proceso))
    return resultados


def obtener_beneficio(resultado):
    """Devuelve el beneficio de un resultado. Se usa para ordenar."""
    return resultado["beneficio"]


def ordenar_por_beneficio(resultados):
    """Devuelve los resultados de mayor a menor beneficio."""
    return sorted(resultados, key=obtener_beneficio, reverse=True)


def filtrar_por_clasificacion(resultados, clasificacion):
    """Devuelve solo los resultados que tienen la clasificación indicada."""
    filtrados = []
    for resultado in resultados:
        if resultado["clasificacion"] == clasificacion:
            filtrados.append(resultado)
    return filtrados


def sumar_horas(resultados):
    """Devuelve la suma de las horas de una lista de resultados."""
    total_horas = 0
    for resultado in resultados:
        total_horas = total_horas + resultado["horas"]
    return round(total_horas, DECIMALES_HORAS)


def mostrar_tabla(titulo, resultados):
    """Muestra en pantalla un título y una tabla con los resultados."""
    print()
    print(titulo)
    print(
        f"{'Proceso':<{ANCHO_NOMBRE}}"
        f"{'Horas':>{ANCHO_COLUMNA}}"
        f"{'Beneficio':>{ANCHO_COLUMNA}}"
        f"{'Complejidad':>{ANCHO_COLUMNA}}"
        f"   Clasificación"
    )
    for resultado in resultados:
        print(
            f"{resultado['nombre']:<{ANCHO_NOMBRE}}"
            f"{resultado['horas']:>{ANCHO_COLUMNA}}"
            f"{resultado['beneficio']:>{ANCHO_COLUMNA}}"
            f"{resultado['complejidad']:>{ANCHO_COLUMNA}}"
            f"   {resultado['clasificacion']}"
        )


def main():
    """Ejecuta el programa completo."""
    resultados = evaluar_procesos(PROCESOS)
    resultados_ordenados = ordenar_por_beneficio(resultados)
    mostrar_tabla("LISTADO COMPLETO DE PROCESOS", resultados_ordenados)

    quick_wins = filtrar_por_clasificacion(
        resultados_ordenados,
        CLASIFICACION_QUICK_WIN,
    )
    mostrar_tabla("PROCESOS QUICK WIN", quick_wins)
    total_horas = sumar_horas(quick_wins)
    print()
    print("Total de horas ahorradas al mes con los Quick Win:", total_horas)


if __name__ == "__main__":
    main()

    