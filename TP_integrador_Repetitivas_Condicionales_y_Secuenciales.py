## Ejercicio 1— “Caja del Kiosco”

# Objetivo: Simular una compra con validaciones y cálculo de total.

#Requisitos

# 1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while).

# 2. Pedir cantidad de productos a comprar (número entero positivo, validar con .isdigit() en while).

# 3. Por cada producto (usar for): 

# o Pedir precio (entero, validar .isdigit()).
# o Pedir si tiene descuento S/N (validar con while, aceptar s o n en cualquier mayuscula/minuscula).
# o Si tiene descuento: aplicar 10% al precio de ese producto.
# 4. Al final mostrar:

# o Total sin descuentos
# o Total con descuentos
# o Ahorro total
# o Promedio por producto (usar float y formatear con :.2f, ejem:
# x = 3.14159
# print(f"{x:.2f}"))

total_sin_descuento = 0
total_con_descuento = 0
ahorro_total = 0

while True:
    nombre = input("Ingrese nombre del cliente: ")
    if nombre != "" and nombre.isalpha():
        break
    else:
        print("Error, Ingrese nombre valido")

while True:
    cantidad = input("Ingrese cantidad de productos: ")
    if cantidad.isdigit() and int(cantidad) > 0:
        cantidad = int(cantidad)
        break
    else:
        print("Error, Ingrese un numero positivo")

for i in range(cantidad):
    print(f"\nProducto {i+1}: ")
    while True:
        precio = input("Ingrese precio: ")

        if precio.isdigit() and int(precio) > 0:
            precio =int(precio)
            break
        else:
            print(f"Error, Ingrese un precio valido")
    
    total_sin_descuento += precio

    while True:
        descuento = input("¿Tiene descuento? (S/N)").lower()

        if descuento in ("s", "n"):
            break
        else:
            print(f"Error, Ingrese S o N")
    if descuento == "s":
        ahorro = precio * .1
        precio_final = precio - ahorro
        ahorro_total += ahorro
    else:
        precio_final = precio
    
    total_con_descuento += precio_final

promedio = total_con_descuento / cantidad

print(f"\nCliente: {nombre}")
print(f"Cantidad de productos: {cantidad}")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro total: ${ahorro_total:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")





### Ejercicio 2 — “Acceso al Campus y Menú Seguro”

usuario_correcto = "alumno"
clave_correcta = "python123"
intentos = 3 

while intentos > 0:
    usuario_intento = input("ingrese nombre usuario: ")
    clave_intento = input("ingrese contraseña: ")

    if usuario_intento == usuario_correcto and clave_intento == clave_correcta:
        while True:
            print ("Menu")
            print ("1.Ver estado de inscripción")
            print ("2.Cambiar clave")
            print ("3.Mostrar mensaje motivacional")
            print ("4.Salir")
            opcion = input("ingrese opcion(1/4): ")
            if opcion.isdigit() and 1 <= int(opcion) <= 4:
                opcion = int(opcion)
                if opcion == 1:
                    print("Inscripto")
                elif opcion == 2:
                    clave_nueva = input("Ingrese nueva contraseña: ")
                    confirmacion = input("Confirme nueva contraseña: ")
                    if clave_nueva == confirmacion:
                        if len(clave_nueva) >=6:
                            print("Cambio de contraseña exitoso")
                            clave_correcta = clave_nueva 
                        else:
                            print("Error,la clave debe tener al menos 6 caracteres")
                    else:
                        print("Error, las claves no o")
                elif opcion == 3:
                    print("La mejor manera de predecir el futuro es crearlo")
                elif opcion == 4:
                    print("saliendo...")
                    break
            else:
                print("Error, opcion invalida")
    else:
        intentos -= 1
        print(f"Usuario o contraseña no concuerdan, te quedan {intentos} intentos.")
        if intentos == 0:
            print("Cuenta bloqueada")


### 3 Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”

# Agenda de Turnos (sin listas)

# Turnos vacíos
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

# Validar nombre del operador
while True:
    operador = input("Ingrese nombre del operador: ")

    if operador != "" and operador.isalpha():
        print(f"Bienvenido/a {operador}")
        break
    else:
        print("Error: ingrese solo letras.")

# Menú principal
while True:
    print("\n--- MENÚ ---")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Ingrese opción (1-5): ")

    if not (opcion.isdigit() and 1 <= int(opcion) <= 5):
        print("Error: opción inválida.")
        continue

    opcion = int(opcion)

    # 1. Reservar turno
    if opcion == 1:

        while True:
            dia = input("Ingrese día (1=Lunes, 2=Martes): ")

            if dia.isdigit() and int(dia) in (1, 2):
                dia = int(dia)
                break
            else:
                print("Error: día inválido.")

        while True:
            paciente = input("Ingrese nombre del paciente: ")

            if paciente != "" and paciente.isalpha():
                break
            else:
                print("Error: ingrese solo letras.")

        if dia == 1:
            # Verificar repetido
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Error: ese paciente ya tiene turno el lunes.")
            else:
                if lunes1 == "":
                    lunes1 = paciente
                    print("Turno reservado en Lunes - Turno 1")
                elif lunes2 == "":
                    lunes2 = paciente
                    print("Turno reservado en Lunes - Turno 2")
                elif lunes3 == "":
                    lunes3 = paciente
                    print("Turno reservado en Lunes - Turno 3")
                elif lunes4 == "":
                    lunes4 = paciente
                    print("Turno reservado en Lunes - Turno 4")
                else:
                    print("No hay cupos disponibles para el lunes.")

        elif dia == 2:
            # Verificar repetido
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Error: ese paciente ya tiene turno el martes.")
            else:
                if martes1 == "":
                    martes1 = paciente
                    print("Turno reservado en Martes - Turno 1")
                elif martes2 == "":
                    martes2 = paciente
                    print("Turno reservado en Martes - Turno 2")
                elif martes3 == "":
                    martes3 = paciente
                    print("Turno reservado en Martes - Turno 3")
                else:
                    print("No hay cupos disponibles para el martes.")

    # 2. Cancelar turno
    elif opcion == 2:

        while True:
            dia = input("Ingrese día (1=Lunes, 2=Martes): ")

            if dia.isdigit() and int(dia) in (1, 2):
                dia = int(dia)
                break
            else:
                print("Error: día inválido.")

        while True:
            paciente = input("Ingrese nombre del paciente a cancelar: ")

            if paciente != "" and paciente.isalpha():
                break
            else:
                print("Error: ingrese solo letras.")

        encontrado = False

        if dia == 1:
            if lunes1 == paciente:
                lunes1 = ""
                encontrado = True
            elif lunes2 == paciente:
                lunes2 = ""
                encontrado = True
            elif lunes3 == paciente:
                lunes3 = ""
                encontrado = True
            elif lunes4 == paciente:
                lunes4 = ""
                encontrado = True

        elif dia == 2:
            if martes1 == paciente:
                martes1 = ""
                encontrado = True
            elif martes2 == paciente:
                martes2 = ""
                encontrado = True
            elif martes3 == paciente:
                martes3 = ""
                encontrado = True

        if encontrado:
            print("Turno cancelado correctamente.")
        else:
            print("Paciente no encontrado.")

    # 3. Ver agenda del día
    elif opcion == 3:

        while True:
            dia = input("Ingrese día (1=Lunes, 2=Martes): ")

            if dia.isdigit() and int(dia) in (1, 2):
                dia = int(dia)
                break
            else:
                print("Error: día inválido.")

        if dia == 1:
            print("\n--- Agenda Lunes ---")
            print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")

        else:
            print("\n--- Agenda Martes ---")
            print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

    # 4. Resumen general
    elif opcion == 4:
        ocupados_lunes = 0
        ocupados_martes = 0

        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1

        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        if martes3 != "":
            ocupados_martes += 1

        disponibles_lunes = 4 - ocupados_lunes
        disponibles_martes = 3 - ocupados_martes

        print("\n--- Resumen General ---")
        print(f"Lunes: ocupados {ocupados_lunes} | disponibles {disponibles_lunes}")
        print(f"Martes: ocupados {ocupados_martes} | disponibles {disponibles_martes}")

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Empate en cantidad de turnos")

    elif opcion == 5:
        print("Cerrando sistema...")
        break

    ### 4 “Escape Room: La Bóveda”

    energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0

# Validar nombre del agente
while True:
    nombre = input("Ingrese nombre del agente: ")

    if nombre != "" and nombre.isalpha():
        print(f"Bienvenido/a, agente {nombre}")
        break
    else:
        print("Error: ingrese solo letras.")

# Juego principal
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    # Regla de bloqueo por alarma
    if alarma and tiempo <= 3:
        print("\n⚠ El sistema se bloqueó por alarma. Has perdido.")
        break

    # Mostrar estado
    print("\n--- ESTADO ACTUAL ---")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Alarma: {'ACTIVA' if alarma else 'APAGADA'}")
    print(f"Código parcial: {codigo_parcial}")

    # Menú
    print("\n1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía, -1 tiempo)")

    while True:
        opcion = input("Ingrese opción (1-3): ")

        if opcion.isdigit() and 1 <= int(opcion) <= 3:
            opcion = int(opcion)
            break
        else:
            print("Error: opción inválida.")

    # Opción 1: Forzar cerradura
    if opcion == 1:
        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        # Regla anti-spam
        if racha_forzar == 3:
            alarma = True
            print("\n⚠ La cerradura se trabó por forzar demasiado. Alarma activada.")
            continue

        # Riesgo de alarma si energía baja
        if energia < 40:
            print("⚠ Riesgo de alarma: elige un número del 1 al 3")

            while True:
                riesgo = input("Número: ")

                if riesgo.isdigit() and 1 <= int(riesgo) <= 3:
                    riesgo = int(riesgo)
                    break
                else:
                    print("Error: ingrese un número entre 1 y 3.")

            if riesgo == 3:
                alarma = True
                print("⚠ Se activó la alarma.")

        if not alarma:
            cerraduras_abiertas += 1
            print("🔓 Cerradura abierta.")

    # Opción 2: Hackear panel
    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        racha_forzar = 0

        print("\nHackeando panel...")
        for paso in range(1, 5):
            print(f"Paso {paso}/4")
            codigo_parcial += "A"

        print(f"Código parcial actual: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("🔓 Hackeo exitoso: se abrió una cerradura.")

    # Opción 3: Descansar
    elif opcion == 3:
        energia += 15
        tiempo -= 1
        racha_forzar = 0

        if energia > 100:
            energia = 100

        if alarma:
            energia -= 10
            print("⚠ La alarma activa consume energía extra.")

        print("Descansaste y recuperaste energía.")

# Resultado final
if cerraduras_abiertas == 3:
    print(f"\n🏆 ¡Victoria, agente {nombre}! Abriste la bóveda.")
elif energia <= 0 or tiempo <= 0:
    print(f"\n💀 Derrota, agente {nombre}. Te quedaste sin recursos.")



######## 5 “Escape Room:"La Arena del Gladiador" ##########

print("--- BIENVENIDO A LA ARENA ---")

# Validar nombre
while True:
    nombre = input("Nombre del Gladiador: ")

    if nombre != "" and nombre.isalpha():
        break
    else:
        print("Error: Solo se permiten letras.")

# Variables iniciales
vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_pesado = 15
danio_enemigo = 12
turno_gladiador = True

print("\n=== INICIO DEL COMBATE ===")

# Ciclo de combate
while vida_jugador > 0 and vida_enemigo > 0:

    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    # Validar opción
    while True:
        opcion = input("Opción: ")

        if opcion.isdigit() and 1 <= int(opcion) <= 3:
            opcion = int(opcion)
            break
        else:
            print("Error: Ingrese un número válido.")

    # Opción 1: Ataque pesado
    if opcion == 1:
        if vida_enemigo < 20:
            danio_final = danio_pesado * 1.5
            print("¡Golpe Crítico!")
        else:
            danio_final = danio_pesado

        vida_enemigo -= danio_final
        print(f"¡Atacaste al enemigo por {danio_final} puntos de daño!")

    # Opción 2: Ráfaga veloz
    elif opcion == 2:
        print(">> ¡Inicias una ráfaga de golpes!")

        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

            if vida_enemigo <= 0:
                break

    # Opción 3: Curar
    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1

            if vida_jugador > 100:
                vida_jugador = 100

            print("¡Te curaste 30 puntos de vida!")
        else:
            print("¡No quedan pociones!")

    # Turno enemigo (solo si sigue vivo)
    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f"¡El enemigo te atacó por {danio_enemigo} puntos de daño!")

# Fin del juego
print("\n=== FIN DEL COMBATE ===")

if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")