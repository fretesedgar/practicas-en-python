nombre=input("Ingresa tu nombre: ")
edad=input("Ingresa tu edad: ")
promedio=input("Ingresa la vida estimada de tu pais: ")
print (f"Tu nombre es: {nombre} y tu edad es {edad} ")
edad=int(edad)
promedio=int(promedio)
dias=promedio-edad
print(f"{nombre}... Te quedan: {dias:,} years to die")