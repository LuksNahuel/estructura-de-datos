# -*- coding: utf-8 -*-
import juzgado
import expediente

def cantidadPorMes(mes):
    salida = 0
    if mes <= 2:
        salida = 250
    elif mes % 2 == 0:
        salida = cantidadPorMes(mes - 1) + cantidadPorMes(mes - 2)
    else:
        salida = cantidadPorMes(mes - 1) * 3 + 20
    return salida

def cantidadHasta_(unMes):
    salida = 0
    if unMes == 1:
        salida = cantidadPorMes(unMes)
    else:
        salida = cantidadPorMes(unMes) + cantidadHasta_(unMes - 1)
    return salida
        
#############################################################
    
juz1 = juzgado.Juzgado(0)
juz2 = juzgado.Juzgado()
juz3 = juzgado.Juzgado()

exp = expediente.Expediente(5, "penal", "urgente")

# El primer elemento siempre es el juzgado de turno
def mesaDeEntradas(juzgadoDeTurno, juzgadoAux0, juzgadoAux1, exp):
    try:
        juzgadoDeTurno.recibirExpediente(exp)
    except:
        if juzgadoAux0.cantidadDeExpedientes() < juzgadoAux1.cantidadDeExpedientes():
            juzgadoAux0.recibirExpediente(exp)
        else:
            juzgadoAux1.recibirExpediente(exp)

mesaDeEntradas(juz1, juz2, juz3, exp)