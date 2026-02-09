print("Este programa captura importes")
info = """

              Calcula tu suma

    Este programa lleva el conteo de cuantos importes ha introducido un usuario.
    
    Va acumulando todos los importes que el usuario ingresa.
    
    Si el usuario desea terminar el programa puede escribir cualquier momento la palabra exit, quit, terminar.
      
                                                         Elaborado por yomilala
                                                         
"""
print(info)
conteo = 0
suma = 0.0
minimo = None
maximo = None

while True:
    user_message = """
    
        Ingresa tu importe (MxN)
        Si quieres dejar tu importe puedes ingresar en cualquier momento
        exit, quit, terminar.
        
    """
    line = input("Ingresa tu importe (MxN)").lower()
    if line ==  "exit" or line == "quit" or line == "terminar":
        break
    try:
        value = float(line)
    except ValueError:
        print("Valor invalido. Intenta de nuevo (ej. 125.6)")
        continue
        
    conteo += 1 # Me dice cuantos numeros he ingresado
    suma+= value # Me lleva la acumulacion
    
    if minimo is None or value < minimo:
        minimo = value
    
    if maximo is None or value > maximo:
        maximo = value
        
if conteo == 0:
    print("No se capturaron importes")
else:
    print("="*32)
    print (f"{conteo}")
    print (f"{suma}")
    print (f"{minimo}")
    print (f"{maximo}")
    
        

print("Programa finalizado")