#Considere el cálculo de la depreciación de un bien depreciable (por ejemplo, un edificio, maquinaria,
#etc.); una de las formas de hacer la depreciación es por el método de la línea recta, el cual consiste
#en dividir el valor total del bien por el número de años de vida útil de éste. El cociente de esta división
#es el valor con el que se deprecia el bien cada año.
#Por ejemplo, si un bien tiene el valor de $8.000.000 y se va a depreciar en 10 años, la depreciación
#anual se calculará: $8.000.000 / 10 = $800.000. Desarrolle un programa que muestre el proceso de depreciación de un bien depreciable por el
#método de la línea recta. El valor inicial, y los años de depreciación serán dados por el usuario.


dp=int(input('Ingrese los años en los que quiere analizar la depreciación: '))
valor=float(input('Ingrese el valor del bien: '))
const=float(valor/dp)
for i in range(dp):
    valor=valor-const
    print('[ año',i+1,']', '|Valor del bien: ',valor,'|')





