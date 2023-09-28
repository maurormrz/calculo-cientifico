def add_time(start, duration, dia_semana=False):

    dias_semana_indice = {"lunes": 0, "martes": 1, "miercoles": 2, "jueves": 3, "viernes": 4, "sabado": 5, "domingo": 6}

    dias_semana_lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

    duracion_tupla = duration.partition(":")
    print(duracion_tupla)
    duracion_horas = int(duracion_tupla[0])
    duracion_minutos = int(duracion_tupla[2])

    comienzo_tupla = start.partition(":")
    comienzo_tupla_minutos = comienzo_tupla[2].partition(" ")
    comienzo_horas = int(comienzo_tupla[0])
    comienzo_minutos = int(comienzo_tupla_minutos[0])
    am_o_pm = comienzo_tupla_minutos[2]
    am_y_pm_vuelta = {"AM": "PM", "PM": "AM"}

    cantidad_dias = int(duracion_horas / 24)

    minutos_finales = comienzo_minutos + duracion_minutos
    if(minutos_finales >= 60):
        comienzo_horas += 1
        minutos_finales = minutos_finales % 60
    cantidad_am_y_pm_vueltas = int((comienzo_horas + duracion_horas) / 12)
    horas_finales = (comienzo_horas + duracion_horas) % 12

    minutos_finales = minutos_finales if minutos_finales > 9 else "0" + str(minutos_finales)
    horas_finales = horas_finales = 12 if horas_finales == 0 else horas_finales
    if(am_o_pm == "PM" and comienzo_horas + (duracion_horas % 12) >= 12):
        cantidad_dias += 1

    am_o_pm = am_y_pm_vuelta(am_o_pm) if cantidad_am_y_pm_vueltas % 2 == 1 else am_o_pm

    returnTiempo = str(horas_finales) + ":" + str(minutos_finales) + " " + am_o_pm
    if(dia_semana):
        dia_semana = dia_semana.lower()
        indice = int((dias_semana_indice[dia_semana]) + cantidad_dias) % 7
        nuevo_dia = dias_semana_lista[indice]
        returnTiempo += ", " + nuevo_dia

    if(cantidad_dias == 1):
        return returnTiempo + " " + "(siguiente día)"
    elif(cantidad_dias > 1):
        return returnTiempo + " (" + str(cantidad_dias) + " días después)"

    return returnTiempo