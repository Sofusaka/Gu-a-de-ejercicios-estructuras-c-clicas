#Desarrolle  un programaque muestre  la  edad  de  la  persona  más  joven  que  asiste  a  un  evento.
#No se conoce por anticipado cuántos serán los asistentes, sólo se sabe que cuando ingrese una edad inválida,
#es decir fueradel rango entre [0...120]se habrá dado por terminado el ingreso al evento.

edad=input('ingrese la edad del participante del evento: ')
edad=int(edad)
x=edad
while edad<=120 and edad>=0:
    edad=int(input('ingrese la edad del participante del evento'))
    y=int(edad)
    if y<x:
        x=y
    if edad>120 and edad<0:
        break

print('termina el ingreso del evento')
print('La edad del menor integrante es: ',x)