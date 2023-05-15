import krpc
from time import sleep
import math


# Función para conectar al servidor KRPC
def connect_server():
    # Intentar conectarse al servidor de forma continua
    while True:
        try:
            # Establecer conexión con el servidor KRPC
            conn = krpc.connect(
                name='Default Server',
                address='127.0.0.1',
                rpc_port=50000, stream_port=50001)
            print("Conexión exitosa al servidor")
            break

        except ConnectionRefusedError:
            # Si no se puede conectar, manejar el error y preguntar si se desea reintentar
            print("No se puede connectar con el servidor.")
            reintentar = ""
            while reintentar.upper() not in ("S", "N"):
                reintentar = input("Reintentar conexión (S/N): ")
                if reintentar.upper() == "N":
                    return None

        sleep(1)  # Pausa entre intentos de conexión

    return conn

# Conectar al servidor KRPC
conn = connect_server()
# Obtener la nave activa
vessel = conn.space_center.active_vessel

# Establecer marcos de referencia orbital y de superficie
orbital_frame = vessel.orbital_reference_frame
vessel_frame = vessel.surface_reference_frame

# Bucle infinito para leer y mostrar la dirección del vector orbital redondeada a centésimas
while True:
    # Obtener información de telemetría de la nave en el marco de referencia orbital
    orbital_telemetry = vessel.flight(orbital_frame)
    # Obtener la dirección del vector orbital
    orbital_direction_vector = orbital_telemetry.direction

    # Redondear cada componente del vector orbital a centésimas
    orbital_direction_vector = tuple(map(lambda x: round(x, 2), orbital_direction_vector))
    odv = orbital_direction_vector

    # Imprimir el vector orbital redondeado
    print(orbital_direction_vector)

    posible_funcion = 1/(1+abs(odv[0])) + odv[1]+ 1/(1+abs(odv[2]))
    print(posible_funcion)


    # Pausar por un segundo antes de actualizar los datos
    sleep(1)
