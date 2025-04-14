"""medir la longitud de las palabras ingresadas.
PALABRAS
anayeli rulfo orosco
20/03/2025-... 21/03/2025
"
 \n" + 
"""
print("""        hola usuario
¡bienvenido al sistema de longitud de palabras!""")
while True:
    palabra=input("por favor ingresa alguna:\n ")

    longitud= len (palabra)#la funcion len, nos indica el tamaño del string.

    if longitud >=4 and longitud <=8:#comparar que longitud "y" palabra... ":" hasta aqui termina la condicional.
        print(f'¡TU PALABRA ES ADECUADA!. \n  {palabra} ESTA EN EL RANGO de 4 a 8 letras. \n' )
        break
    elif longitud < 4:
        print(f"""a tu palabra {palabra} LE HACEN FALTA LETRAS para cumplir el rango de la longitud. 
            
           {palabra} solo tiene {longitud} letras. 

              ¡intenta nuevamente! \n """)
        
    elif longitud > 8:
        print(f"""a tu palabra {palabra} LE SOBRAN LETRAS para cumplir el rango de la longitud. 
              
            ya que tiene {longitud} letras.

              ¡intenta nuevamente! \n """)

print(f'la palabra "{palabra}" tiene {longitud} letras.')

#CODIGO TERMINADO
#RECUERDA PONER SIEMPRE DESPUES DE ALGUNA MODIFICACION IMPORTANTE  CTRL +S, PARA GUARDAR LOS CAMBIOS

#en la funcion len, al escribir los caracteres, cuenta desde todo incluido los espacios.
#la funcion input implica que puedes agregar cualquier caracter (numeros, letras, signos, etc) y lo guarda como dato.
#los metodos 1,strip(quita los espacios en blanco, es decir tanto adelantre y atras), 2 lstrip(quita los primeros de la izquierda) , 3, rstrip(los del final a la derecha.);metodo de transformacion de cadenas. 


#para volver a realizar un paso lo que debemos hacer es... añadimos un bucle while true, donde nos marca que si queremos repetir una bloque de codigo hasta que sea verdadera o cumpla alguno de los elif pase a 
