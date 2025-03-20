# Importamos la librería pywhatkit para enviar mensajes de WhatsApp
import pywhatkit

try:
    # Solicitamos al usuario el número de teléfono con el prefijo del país
    usuario_telefono = input("Ingrese el número de teléfono (con el prefijo + de tu país): ").strip()
    
    # Solicitamos el mensaje que desea enviar
    usuario_mensaje = input("Ingrese el mensaje que desea enviar: ").strip()

    # Solicitamos la hora y el minuto en los que se enviará el mensaje y los convertimos a enteros
    usuario_hora = int(input("Ingrese la hora a la que desea enviar el mensaje (formato HH:MM): "))
    usuario_minuto = int(input("Ingrese el minuto a la que desea enviar el mensaje (formato HH:MM): "))

    # Validamos que el número de teléfono sea correcto:
    # 1. Debe comenzar con "+"
    # 2. Después del "+" solo debe contener números
    if not usuario_telefono.startswith("+") or not usuario_telefono[1:].isdigit():
        raise ValueError("El número de teléfono debe comenzar con el prefijo + de tu país y contener solo números.")

    # Validamos que el mensaje no esté vacío
    if not usuario_mensaje:
        raise ValueError("El mensaje no puede estar vacío.")
    
    # Validamos que la hora y el minuto sean valores numéricos válidos
    if not usuario_hora or not usuario_minuto:
        raise ValueError("La hora y el minuto deben ser números.")

    # Si todas las validaciones pasan, enviamos el mensaje en el horario especificado
    pywhatkit.sendwhatmsg(usuario_telefono, usuario_mensaje, usuario_hora, usuario_minuto)
    print("Mensaje enviado.")

# Capturamos errores generales que puedan ocurrir durante la ejecución del programa
except Exception as error:
    print(f"Error del programa: {error}.")

# Capturamos errores específicos relacionados con la validación de los datos ingresados por el usuario
except ValueError as error:
    print(f"Error del usuario: {error}.")
