print("Operaciones con fracciones a/b+1")
#Siempre complementar el input con int o float para convertirlo a numero
a=float(input("Ingresa el valor a: "))
b=float(input("Ingresa el valor b: "))
res=a/b+1
#Se ingresa la coma primeramente para agregar , a la impresion y el .2 es para visualizar
#dos decimales
print(f"El valor es: {res:,.2f}")