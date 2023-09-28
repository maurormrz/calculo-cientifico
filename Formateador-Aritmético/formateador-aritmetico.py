import re

def arithmetic_arranger(problems, solucion = False):

    if not problems:
        return ""

    primero = ""
    segundo = ""
    lineas = ""
    sumax = ""
    cadena = ""
    for problema in problems:
        if (re.search("[^\s0-9.+-", problema)):
            if (re.search("[/]", problema) or re.search("[*]", problema)):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."

        primerNumero = problema.split(" ")[0]
        operador = problema.split(" ")[1]
        segundoNumero = problema.split(" ")[2]

        if(len(primerNumero) >= 5 or len(segundoNumero) >= 5):
            return "Error: Numbers cannot be more than four digits."

        suma = ""
        if(operador == "+"):
            suma = str(int(primerNumero) + int(segundoNumero))
        elif(operador == "-"):
            suma = str(int(primerNumero) - int(segundoNumero))

        longitud = max(len(primerNumero), len(segundoNumero)) + 2
        arriba = str(primerNumero).rjust(longitud)
        debajo = operador + str(segundoNumero).rjust(longitud - 1)
        linea = ""
        resultado = str(suma).rjust(longitud)
        for s in range (longitud):
            linea += "-"

        if problema != problems[-1]:
            primero += arriba + "   "
            segundo += debajo + "   "
            lineas += linea + "   "
            sumax += resultado + "   "
        else:
            primero += arriba
            segundo += debajo
            lineas += linea
            sumax += resultado 

    if solucion:
        cadena = primero + "\n" + segundo + "\n" + lineas + "\n" + sumax
    else:
        cadena = primero + "\n" + segundo + "\n" + linea
    return cadena