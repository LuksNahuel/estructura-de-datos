import expediente
import juzgado

moron = juzgado.Juzgado()

moron.recibirExpediente(expediente.Expediente(1, "penal", "urgente"))
moron.recibirExpediente(expediente.Expediente(45, "civil", "urgente"))
moron.recibirExpediente(expediente.Expediente(22, "criminal", "urgente"))
moron.recibirExpediente(expediente.Expediente(15, "penal", "normal"))
moron.recibirExpediente(expediente.Expediente(13, "civil", "normal"))
moron.recibirExpediente(expediente.Expediente(19, "criminal", "normal"))

print("El juzgado de Morón tiene %s expedientes." % moron.cantidadDeExpedientes())

print(moron.cantidadPorTipo("criminal"))

print(moron.estaComplicado())

print(moron.primerExpedienteATratar())

print("Los expedientes normales son", moron.normales)

print("Los expedientes urgentes son", moron.urgentes)

moron.cambiaDeEstado(15)

print("Los expedientes normales quedaron así", moron.normales)
print("Los expedientes urgentes quedaron así", moron.urgentes)