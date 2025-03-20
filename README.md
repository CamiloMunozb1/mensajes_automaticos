# Automatización de Mensajes de WhatsApp con Python

Este proyecto permite enviar mensajes automáticamente por WhatsApp usando la librería `pywhatkit`. Puedes ingresar un número de teléfono, un mensaje y programar la hora exacta para su envío.

## Requisitos

- Python 3.7 o superior
- Tener una sesión iniciada en WhatsApp Web
- Conexión a Internet

## Instalación

1. Clona este repositorio o descarga los archivos:
   ```sh
   git clone https://github.com/tu_usuario/tu_repositorio.git
   ```
2. Instala las dependencias necesarias:
   ```sh
   pip install pywhatkit
   ```

## Uso

Ejecuta el script y sigue las instrucciones:
```sh
python script.py
```

El programa te pedirá:
1. **Número de teléfono** con prefijo del país (Ej: `+573001234567`)
2. **Mensaje** que deseas enviar
3. **Hora y minuto** en que deseas enviarlo

## Ejemplo de Uso

```sh
Ingrese el número de teléfono (con el prefijo + de tu país): +573001234567
Ingrese el mensaje que desea enviar: Hola, esto es una prueba de automatización.
Ingrese la hora a la que desea enviar el mensaje (formato HH:MM): 15
Ingrese el minuto a la que desea enviar el mensaje (formato HH:MM): 30
Mensaje enviado.
```

## Notas
- Asegúrate de que la hora y los minutos ingresados sean válidos.
- La aplicación abrirá WhatsApp Web para enviar el mensaje.
- Si tienes problemas con la configuración, revisa las variables de entorno de Python.

## Contribuciones
Si deseas mejorar este proyecto, siéntete libre de hacer un fork y enviar tus pull requests.

## Autor
Hecho por Juan Camilo Muñoz 

## Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo y modificarlo libremente.

