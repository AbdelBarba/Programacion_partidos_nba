from datetime import date

def obtener_temporada_actual():
    hoy = date.today()
    año = hoy.year
    mes = hoy.month

    if mes >= 10:
        inicio = año
        fin = año + 1
    else:
        inicio = año - 1
        fin = año

    return f"{inicio}-{str(fin)[-2:]}"