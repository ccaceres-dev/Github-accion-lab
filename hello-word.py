import os

# Obtiene la variable del entorno; si no existe, usa "Desconocido"
nombre_usuario = os.getenv('VAR_NOMBRE', 'Desconocido')

print(f"Hola {nombre_usuario}, saludos desde Github actions 🚀")
