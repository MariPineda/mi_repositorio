"""Haremos un script que printee un argumento las veces que se indique por argumento, es decir, si paso los argumentos "Hola y 5, se imprimirá 5 veces "Hola
"""
import sys
argumentos = sys.argv
print(f"nombre del script {sys.argv[0]}")

for i in range(int(sys.argv[2])):
    print(f"{i} : {sys.argv[1]}")