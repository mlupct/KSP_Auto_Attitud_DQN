import krpc
from time import sleep

def connect_server():
    while True:
        try:
            conn = krpc.connect(
                name='Default Server',
                address='127.0.0.1',
                rpc_port=50000, stream_port=50001)
            print("Conexión exitosa al servidor")
            break

        except ConnectionRefusedError:
            print("No se puede connectar con el servidor.")
            reintentar = ""
            while reintentar.upper() not in ("S", "N"):
                reintentar = input("Reintentar conexión (S/N): ")
                if reintentar.upper() == "N":
                    return None

        sleep(1)  # Pausa entre intentos de conexión

    return conn


connect_server()

