"""Hacer un script"""
import sys

print("Los argumentos son: {sys.argv}")

argumentos = sys.argv

if len(argumentos) < 4:
    print ("Error -- faltan argumentos")
    exit (1)

for arg in argumentos:
    print(arg)
file = open(argumentos [1], "a")
#file = open("invitados.txt")
file.write(f"{argumentos[2]} : {argumentos[3]}\n")
file.close()