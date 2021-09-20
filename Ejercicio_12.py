#Existe una serie conocida como la serie de ULAM (en honor al matemático S. Ulam):
#Comience con cualquier entero positivo
#-Si es par, divídalo en 2; si es impar, multiplíquelo por 3 y agréguele 1.
#-Obtenga enteros sucesivamente repitiendo el proceso.
#-Al final obtendrá el número 1, independientemente del entero inicial.
#Por ejemplo: cuando el entero inicial es 26, la secuencia será:
#26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1.
#Desarrolle un programa que lea un entero positivo y obtenga e imprima la sucesión de ULAM.

num=int(input('Digite un entero positivo para obtener su sucesion de ULAM: '))

while num!='a':
    if num<=0:
        num=int(input('usted ha ingresado un numero incorrecto, por favor, ingrese otro numero: '))

    if num!=1:
            if num%2==0:
                num=num/2
                print(num)
            else:
                num=num*3+1
                print(num)
    else:
        break
     
    

    

