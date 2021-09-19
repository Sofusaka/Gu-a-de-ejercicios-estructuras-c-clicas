#Una persona desea invertir su dinero en un banco. El tipo de producto que eligió le da una
#rentabilidad del 2% mensual, y esta cantidad es reinvertida automáticamente; este sistema de
#ahorro elegido tiene una duración de un año. Muestre mes a mes cuánto es el dinero que va
#acumulando, y cuánto es el interés que va generando. Indique al final cuánto dinero le entregarán
#a este ahorrador.

interes=0.02
interes1=0
Inversion=0
Inversion=float(input('Ingrese la cantidad de dinero que desea invertir: '))
for i in range(12):
    interes1=Inversion*interes
    Inversion=Inversion+Inversion*interes
    total1=+Inversion
    print('[mes',i+1,']', 'interes ganado:', round(interes1, 3), '|Valor acumulado:',round(Inversion,3),'|')
    
        











