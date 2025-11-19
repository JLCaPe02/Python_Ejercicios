'''Escriba un programa que simule un inicio de sesión solicitando el nombre de usuario y
contraseña, y mostrar un mensaje en pantalla, inicio de sesión correcto/ nombre de usuario
incorrecto'''

correcto = 0
u_correcto = "usuario"
p_correcto = "password"

while correcto == 0:
    user = input("Introduzca el nombre de usuario")
    passw = input("Introduzca tu contraseña")

    if user == u_correcto and passw == p_correcto:
        correcto += 1
        print("Inicio de sesión correcto")
    else:
        print("Usuario/Contraseña incorrecto/s")
