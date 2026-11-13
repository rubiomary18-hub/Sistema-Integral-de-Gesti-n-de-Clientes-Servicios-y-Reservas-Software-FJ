
"""
Archivo: main.py

Este módulo ejecuta el programa principal y realiza operaciones de prueba para comprobar su funcionamiento.
"""

# Importamos la clase que administra el sistema.
from sistema import SistemaGestion

# Importamos la clase cliente.
from clientes import Cliente

# Importamos los tres servicios especializados.
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada

# Importamos las funciones de registro.
from registro_logs import registrar_evento, registrar_error


# -----------------------------------------
# FUNCIÓN PARA EJECUTAR OPERACIONES
# -----------------------------------------

def ejecutar_operacion(numero, descripcion, operacion):
    """
    Ejecuta una operación y controla los errores para evitar que el programa se detenga.
    """

    print(f"\nOPERACIÓN {numero}: {descripcion}")

    try:
        resultado = operacion()

    except Exception as error:
        print(f"Error controlado: {error}")
        registrar_error(f"Operación {numero} fallida: {descripcion}", error)

    else:
        print("Operación realizada correctamente.")

        if resultado is not None:
            print(resultado)

        registrar_evento(f"Operación {numero} exitosa: {descripcion}")

    finally:
        print(f"Finalización de la operación {numero}.")


# -----------------------------------------
# PROGRAMA PRINCIPAL
# -----------------------------------------

def main():
    """
    Inicializa el sistema y ejecuta las operaciones de prueba.
    """

    print("=" * 60)
    print("SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ")
    print("=" * 60)

    registrar_evento("Inicio de las pruebas del sistema Software FJ.")

    # Creamos el administrador principal del sistema.
    sistema = SistemaGestion()

    # -----------------------------------------
    # OPERACIONES DE PRUEBA
    # -----------------------------------------

operaciones = [

    ("Registrar cliente María", lambda: sistema.registrar_cliente(Cliente("C001", "María Oviedo", "maria@gmail.com", "3001234567", "Bogotá"))),

    ("Registrar cliente Carlos", lambda: sistema.registrar_cliente(Cliente("C002", "Carlos Callejas", "carlos@gmail.com", "3101234567", "Medellín"))),

    ("Intentar registrar un cliente con correo incorrecto", lambda: sistema.registrar_cliente(Cliente("C003", "Erika Gómez", "correo_incorrecto", "3201234567", "Cali"))),

    ("Intentar registrar un cliente duplicado", lambda: sistema.registrar_cliente(Cliente("C001", "María Oviedo", "otra@gmail.com", "3001234567", "Bogotá"))),

    ("Registrar servicio de reserva de sala", lambda: sistema.registrar_servicio(ReservaSala("S001", "Sala de reuniones", 50000, 20))),

    ("Registrar servicio de alquiler de equipos", lambda: sistema.registrar_servicio(AlquilerEquipo("S002", "Alquiler de computador", 40000, "Computador"))),

    ("Registrar servicio de asesoría especializada", lambda: sistema.registrar_servicio(AsesoriaEspecializada("S003", "Asesoría tecnológica", 80000, "Sistemas"))),

    ("Intentar registrar un servicio con precio incorrecto", lambda: sistema.registrar_servicio(ReservaSala("S004", "Sala inválida", -50000, 15))),

    ("Crear una reserva válida", lambda: sistema.crear_reserva("R001", "C001", "S001", 3)),

    ("Crear otra reserva válida", lambda: sistema.crear_reserva("R002", "C002", "S002", 2)),

    ("Intentar crear una reserva con duración incorrecta", lambda: sistema.crear_reserva("R003", "C001", "S001", -2)),

    ("Confirmar la primera reserva", lambda: sistema.buscar_reserva("R001").confirmar()),

    ("Procesar la primera reserva y calcular su costo", lambda: sistema.buscar_reserva("R001").procesar()),

    ("Cancelar la segunda reserva", lambda: sistema.buscar_reserva("R002").cancelar()),

    ("Intentar procesar una reserva cancelada", lambda: sistema.buscar_reserva("R002").procesar()),

    ("Buscar un cliente inexistente", lambda: sistema.buscar_cliente(id_cliente="C999"))
]

    # -----------------------------------------
    # EJECUCIÓN DE LAS OPERACIONES
    # -----------------------------------------

    for numero, (descripcion, operacion) in enumerate(operaciones, start=1):
        ejecutar_operacion(numero, descripcion, operacion)

    # -----------------------------------------
    # MOSTRAR INFORMACIÓN FINAL
    # -----------------------------------------

    print("\n" + "=" * 60)
    print("RESUMEN FINAL DEL SISTEMA")
    print("=" * 60)

    print(f"\nClientes registrados: {len(sistema.listar_clientes())}")
    print(f"Servicios registrados: {len(sistema.listar_servicios())}")
    print(f"Reservas registradas: {len(sistema.listar_reservas())}")

    print("\nINFORMACIÓN DE LOS CLIENTES")

    for cliente in sistema.listar_clientes():
        print("\n" + cliente.mostrar_informacion())

    print("\nINFORMACIÓN DE LOS SERVICIOS")

    for servicio in sistema.listar_servicios():
        print("\n" + servicio.mostrar_informacion())

    print("\nINFORMACIÓN DE LAS RESERVAS")

    for reserva in sistema.listar_reservas():
        print("\n" + reserva.mostrar_informacion())

    registrar_evento("Finalización de las pruebas del sistema Software FJ.")

    print("\n" + "=" * 60)
    print("PROGRAMA FINALIZADO")
    print("=" * 60)


# -----------------------------------------
# PUNTO DE ENTRADA DEL PROGRAMA
# -----------------------------------------

if __name__ == "__main__":
    main()
