pregunta = int(input('Trabajas desde casa?'))

if (pregunta==1):
    print ("Eres afortunado")
if (pregunta==2):
    print ("Trabajas fuera de casa")

    tiempo= int(input("Cuantos minutos haces en el trabajo?"))
    if (tiempo==0):
        print ("Trabajas desde casa")

    elif (tiempo <=20):
        print ("Es poco tiempo!")
    elif (tiempo >= 21 and tiempo <=45):
        print ("Es un tiempo razonable")
    else:
        print ("Busca otras rutas")
