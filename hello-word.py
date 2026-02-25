import os

# Leemos la variable de entorno que definiremos en el YAML
nombre = os.getenv('VAR_NOMBRE', 'Usuario')

print(f"Hola {nombre}, saludos desde Github actions")
