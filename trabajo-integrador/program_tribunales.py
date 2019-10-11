# -*- coding: utf-8 -*-
import tribunales
import juzgado 
import expediente

tribunal = tribunales.Tribunales(4, 4)

moron = juzgado.Juzgado(nombre = "Moron")
moron.recibirExpediente(expediente.Expediente(3, "penal", "urgente"))
moron.recibirExpediente(expediente.Expediente(4, "civil", "urgente"))
moron.recibirExpediente(expediente.Expediente(5, "penal", "normal"))

merlo = juzgado.Juzgado(nombre = "Merlo")
merlo.recibirExpediente(expediente.Expediente(1, "penal", "normal"))

sanjusto = juzgado.Juzgado(nombre = "San Justo")

capital = juzgado.Juzgado(nombre = "Capital")


tribunal.establecerJuzgadoEn(0, 3, moron)
tribunal.establecerJuzgadoEn(0, 1, merlo)
tribunal.establecerJuzgadoEn(0, 0, sanjusto)
tribunal.establecerJuzgadoEn(3, 0, capital)
tribunal.establecerJuzgadoEn(2, 1, juzgado.Juzgado(nombre = "Chacarita"))

recargado = tribunal.juzgadoMasRecargado(0)

complicados = tribunal.cantidadDeJuzgadosComplicados(0)

listos = tribunal.subirEdificio()

listos1 = tribunal.recorrerOficinas()