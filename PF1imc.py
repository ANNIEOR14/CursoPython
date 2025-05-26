"""
el usuario ingresará sus datos para verificar su tipo de
indice de masa corporal.

INDICE DE MASA CORPORAL.

anayeli rulfo orosco
03/03/2025
"""
 

#DATOS DE EL USUARIO.
print("hola usuario, vamos a tomar tus datos.") #PRINT:ES PARA IMPRIMIR EN LA PANTALLA.
nombre1 = input("¿ Cuál es tu nombre ?: \n") #LA FUNCION INPUT,
#Funcion para interactuar con el usuario,
#necesario para guardar la informacion solicitada.
 
nombre2 = input("¿ Cuál es tu primer apellido ?: \n") #\n es para generar un salto de linea.

nombre3 = input("¿ Cuál es tu segundo apellido ?: \n")

print("hola, mucho gusto " + nombre1 + " " + nombre2 + " " + nombre3 + ", " + "gracias por ingresar tus datos. \n")
#usar simbolos(+) para dividir tipos(variables con cadena de texto.)

#solicitud de datos al usuario.
edad = int(input("¿Cuántos años tienes?: \n"))
print("¡tienes " + " " + str (edad) + " " + "años, increible!\n") 

estatura = int(input("Por favor, ingresa tu estatura en unidad de centimetros: \n")) 
#aqui añadimos los datos en tipo entero(int).

print("¡tu estatura es: " + str(estatura) + " " + "centimetros, genial! \n")
#aqui se imprimiran los datos ingresados.

estaturaImc= estatura/100 #aqui convertiremos los centimetros a metros dividiendo el dato ingresado entre 100.

peso = int(input("Por ultimo necesito que ingreses tu peso en unidad de kilogramos por favor: "))
print("¡gracias¡, tu peso es: " + str(peso) + " "  +  "kilogramos \n")

    
print("!¡muchas gracias por responder las preguntas. \n" 
"Ahora evaluare los datos para sacar el equivalente de tu indice de masa corporal! \n")
#al obtener los datos sugeridos, ejecutaremos cada operacion.
IMC = peso / estaturaImc**2 # escribir "IMC" con mayusculas indica que es una constante,
#y que esta formula es usada mundialmente para evaluar el peso de las personas.
imcFormat = f"{IMC:.2f}" 
# el ´f"{}"´ f-string es una forma de formatear cadenas de texto para poder incrustarlo en una cadena de texto.
# con el ".2f" : indicamos que del resultado, solo tomaremos 2 decimales después del punto.

# "imcFormat" incluye datos tipo int, con "str(variable)" podremos imprimir como cadena de texto. 
print("Con el indice de masa corporal; nos indica que " + str(imcFormat) )

#con las siguientes condiciones, podemos ver a que categoria corresponde cada uno de los resultados.
if IMC >= 0 and IMC <= 15.99: 
#es decir, que si el resultado guardado
#en la variable "IMC" es mayor o igual a cero
#y es menor o igual a 15.99, entonces tiene delgadez severa. 
    print("usted tiene DELGADEZ SEVERA")
elif IMC >= 16.00 and IMC <= 16.99:
    print("usted tiene DELGADEZ MODERADA")
elif IMC >= 17.00 and IMC <= 18.49:
    print("usted tiene DELGADEZ LEVE")
elif IMC >= 18.50 and IMC <= 24.99:
    print("usted tiene un indice de masa corporal NORMAL")
elif IMC >= 25.00 and IMC <= 29.99:
    print("usted tiene SOBRE PESO")
elif IMC >= 30.00 and IMC <= 34.99:
    print("usted tiene OBESIDAD LEVE")
elif IMC >= 35.00 and IMC <= 39.00:
    print("usted tiene OBESIDAD MEDIA")
elif IMC >= 40.00:
    print("usted tiene OBESIDAD MÓRBIDA")


print("No olvides que NO ES NECESARIO sentirse mal para recibir atencion médica.\n")