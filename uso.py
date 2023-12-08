#import funciones_matemáticas

#print (funciones_matemáticas.suma(5,5))
#print (funciones_matemáticas.resta(10,5))
#print (funciones_matemáticas.pi)

#import funciones_matemáticas as fm
#print (fm.suma(10,5))
#print (fm.resta(10,5))
#print (fm.pi)

from funciones_matemáticas import suma, resta, Alumno
alumno = Alumno("Pablo", 10)
alumno.imprimir()
#print (suma(10,5))
#print (resta(10,5))
