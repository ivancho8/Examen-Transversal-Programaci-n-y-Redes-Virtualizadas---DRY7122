from geopy.distance import geodesic
from geopy.point import Point

# Coordenadas geográficas de Santiago de Chile (-33.4489° S, -70.6693° W)
ciudad_origen = Point(-33.4489, -70.6693)

# Coordenadas geográficas de Buenos Aires, Argentina (-34.6037° S, -58.3816° W)
ciudad_destino = Point(-34.6037, -58.3816)

# Calcular la distancia entre las ciudades
distancia = geodesic(ciudad_origen, ciudad_destino).kilometers

# Redondear la distancia a 1 decimal
distancia_redondeada = round(distancia, 1)

# Imprimir la letra S
print("S")

# Imprimir la narrativa del viaje
print(f"Viaje desde Santiago de Chile (-33.4489° S, -70.6693° W) hasta Buenos Aires, Argentina (-34.6037° S, -58.3816° W)")
print(f"Distancia: {distancia_redondeada} kilómetros")
