from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from datetime import timedelta

# Crear un objeto geocoder
geocoder = Nominatim(user_agent="calculo_geografico")

# Solicitar la ciudad de origen al usuario
ciudad_origen_nombre = input("Ingrese la ciudad de origen: ")

# Obtener la ubicación de la ciudad de origen
ubicacion_origen = geocoder.geocode(ciudad_origen_nombre)
latitud_origen, longitud_origen = ubicacion_origen.latitude, ubicacion_origen.longitude

# Solicitar la ciudad de destino al usuario
ciudad_destino_nombre = input("Ingrese la ciudad de destino: ")

# Obtener la ubicación de la ciudad de destino
ubicacion_destino = geocoder.geocode(ciudad_destino_nombre)
latitud_destino, longitud_destino = ubicacion_destino.latitude, ubicacion_destino.longitude

# Calcular la distancia entre las ciudades
distancia = geodesic((latitud_origen, longitud_origen), (latitud_destino, longitud_destino)).kilometers

# Redondear la distancia a 1 decimal
distancia_redondeada = round(distancia, 1)

# Calcular la duración estimada del viaje (suponiendo una velocidad promedio de 60 km/h)
velocidad_promedio = 60  # km/h
duracion_horas = distancia / velocidad_promedio
duracion_timedelta = timedelta(hours=duracion_horas)
duracion_horas_minutos_segundos = str(duracion_timedelta).split(".")[0]

# Calcular el combustible requerido (suponiendo un consumo de 12 km/l)
consumo_combustible = 12  # km/l
combustible_requerido = distancia / consumo_combustible

# Imprimir la letra S
print("S")

# Imprimir la narrativa del viaje
print(f"Viaje desde {ciudad_origen_nombre} ({latitud_origen}°, {longitud_origen}°) hasta {ciudad_destino_nombre} ({latitud_destino}°, {longitud_destino}°)")
print(f"Distancia: {distancia_redondeada} kilómetros")
print(f"Duración estimada: {duracion_horas_minutos_segundos}")
print(f"Combustible requerido: {combustible_requerido} litros")
