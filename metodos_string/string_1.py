mensaje="      Bienvenidos... al curso de Python 😎"
#print(mensaje)

#print("la cantidad de letras en el mensaje es:", len(mensaje))

sinEspacios = mensaje.strip()
#print(sinEspacios)
#print("La cantidad de letras sin espacios es de: ",len(sinEspacios))

#print("texto en mayuscula sostenida: ",sinEspacios.upper())

#print("texto en minuscula: ",sinEspacios.lower())
#print("letra inicial en mayuscula: ",sinEspacios.capitalize())
#print("letra inicial de cada palabra en mayus: ",sinEspacios.title())

parrafo = sinEspacios.split("...")
print(parrafo)
print(parrafo[0])
print(parrafo[1])

