def triangle():
    """
    Ejercicio 8 - Validar Triángulo

    Leer tres números que representan los lados de un triángulo mediante input().
    Verificar si pueden formar un triángulo válido e imprimir el resultado.
    Un triángulo es válido si la suma de dos lados cualesquiera es estrictamente mayor
    que el tercer lado (desigualdad triangular). Si la suma es igual, forman una línea
    recta, no un triángulo.

    Ejemplo:
        Para las entradas "3", "4" y "5", la salida esperada es:
        Los lados forman un triangulo valido

        Para las entradas "1", "2" y "5", la salida esperada es:
        Los lados no forman un triangulo valido
    """
    pass
    lado_uno = float(input())
    lado_dos = float(input())
    lado_tres = float(input())
    
    if lado_uno + lado_dos > lado_tres and lado_uno + lado_tres > lado_dos and lado_dos + lado_tres > lado_uno:
        print("Los lados forman un triangulo valido")
    
    else:
        print("Los lados no forman un triangulo valido")
