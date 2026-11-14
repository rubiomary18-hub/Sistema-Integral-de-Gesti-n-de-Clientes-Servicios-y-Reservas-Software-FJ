
"""
Archivo: sistema.py

Este módulo administra los clientes, servicios y reservas mediante listas y controla las operaciones del sistema.
"""

# Importamos las clases principales.
from clientes import Cliente
from servicios import Servicio
from reservas import Reserva

# Importamos las excepciones personalizadas.
from excepciones import (DatosInvalidosError,ClienteNoEncontradoError,ServicioNoDisponibleError,ReservaInvalidaError)

# Importamos las funciones para registrar eventos y errores.
from registro_logs import registrar_evento, registrar_error


class SistemaGestion:
    """
    Clase principal encargada de administrar el sistema Software FJ.
    """

    def __init__(self):
        """
        Inicializa las listas donde se almacenarán los objetos.
        """

        # Listas para almacenar los clientes, servicios y reservas.
        self._clientes = []
        self._servicios = []
        self._reservas = []

        registrar_evento("Sistema Software FJ inicializado correctamente.")

    # -----------------------------------------
    # REGISTRAR CLIENTES
    # -----------------------------------------

    def registrar_cliente(self, cliente):
        """
        Registra un cliente después de validar sus datos.
        """

        try:
            if not isinstance(cliente, Cliente):
                raise DatosInvalidosError("El objeto proporcionado no corresponde a un cliente válido.")

            if any(c.id_entidad == cliente.id_entidad for c in self._clientes):
                raise DatosInvalidosError("Ya existe un cliente registrado con ese identificador.")

            self._clientes.append(cliente)

            registrar_evento(f"Cliente registrado: {cliente.id_entidad} - {cliente.nombre}.")

            return "Cliente registrado correctamente."

        except Exception as error:
            registrar_error("Error al registrar un cliente", error)
            raise

    # -----------------------------------------
    # BUSCAR CLIENTES
    # -----------------------------------------

    def buscar_cliente(self, id_cliente=None, correo=None):
        """
        Busca un cliente por identificador o por correo electrónico permitiendo dos formas de búsqueda mediante parámetros opcionales.
        """

        try:
            if (id_cliente is None and correo is None) or (id_cliente is not None and correo is not None):
                raise DatosInvalidosError("Debe proporcionar un identificador o un correo, pero no ambos.")

            if id_cliente is not None:
                for cliente in self._clientes:
                   if cliente.id_entidad == str(id_cliente).strip():
    registrar_evento(f"Cliente encontrado: {cliente.id_entidad} - {cliente.nombre}.")
    return cliente

            else:
                if not isinstance(correo, str) or not correo.strip():
                    raise DatosInvalidosError("El correo proporcionado no es válido.")

                for cliente in self._clientes:
                    if cliente.correo == correo.strip().lower():
    registrar_evento(f"Cliente encontrado mediante correo: {cliente.correo}.")
    return cliente
            raise ClienteNoEncontradoError("No se encontró un cliente con los datos proporcionados.")

        except Exception as error:
            registrar_error("Error durante la búsqueda de un cliente", error)
            raise

    # -----------------------------------------
    # REGISTRAR SERVICIOS
    # -----------------------------------------

    def registrar_servicio(self, servicio):
        """
        Registra un servicio especializado en el sistema.
        """

        try:
            if not isinstance(servicio, Servicio):
                raise ServicioNoDisponibleError("El objeto proporcionado no corresponde a un servicio válido.")

            if any(s.id_entidad == servicio.id_entidad for s in self._servicios):
                raise DatosInvalidosError("Ya existe un servicio con ese identificador.")

            self._servicios.append(servicio)

            registrar_evento(f"Servicio registrado: {servicio.id_entidad} - {servicio.nombre}.")

            return "Servicio registrado correctamente."

        except Exception as error:
            registrar_error("Error al registrar un servicio", error)
            raise

    # -----------------------------------------
    # BUSCAR SERVICIOS
    # -----------------------------------------

    def buscar_servicio(self, id_servicio=None, nombre=None):
        """
        Busca un servicio por identificador o por nombre.
        """

        try:
            if (id_servicio is None and nombre is None) or (id_servicio is not None and nombre is not None):
                raise DatosInvalidosError("Debe proporcionar un identificador o un nombre, pero no ambos.")

            if id_servicio is not None:
                for servicio in self._servicios:
                    if servicio.id_entidad == str(id_servicio).strip():
    registrar_evento(f"Servicio encontrado: {servicio.id_entidad} - {servicio.nombre}.")
    return servicio

            else:
                if not isinstance(nombre, str) or not nombre.strip():
                    raise DatosInvalidosError("El nombre del servicio no es válido.")

                for servicio in self._servicios:
                    if servicio.nombre.lower() == nombre.strip().lower():
    registrar_evento(f"Servicio encontrado mediante nombre: {servicio.nombre}.")
    return servicio

            raise ServicioNoDisponibleError("No se encontró el servicio solicitado.")

        except Exception as error:
            registrar_error("Error durante la búsqueda de un servicio", error)
            raise

    # -----------------------------------------
    # CREAR RESERVAS
    # -----------------------------------------

    def crear_reserva(self, id_reserva, id_cliente, id_servicio, duracion):
        """
        Crea una reserva asociando un cliente con un servicio.
        """

        try:
            if any(r.id_entidad == str(id_reserva).strip() for r in self._reservas):
                raise ReservaInvalidaError("Ya existe una reserva con ese identificador.")

            cliente = self.buscar_cliente(id_cliente=id_cliente)
            servicio = self.buscar_servicio(id_servicio=id_servicio)

            reserva = Reserva(id_reserva,cliente,servicio,duracion)

            self._reservas.append(reserva)

            registrar_evento(f"Reserva creada: {reserva.id_entidad} para el cliente {cliente.nombre}.")

            return reserva

        except Exception as error:
            registrar_error("Error al crear una reserva", error)
            raise

    # -----------------------------------------
    # BUSCAR RESERVAS
    # -----------------------------------------

    def buscar_reserva(self, id_reserva):
        """
        Busca una reserva mediante su identificador.
        """

        try:
            for reserva in self._reservas:
                if reserva.id_entidad == str(id_reserva).strip():
                    return reserva

            raise ReservaInvalidaError("No se encontró la reserva solicitada.")

        except Exception as error:
            registrar_error("Error durante la búsqueda de una reserva", error)
            raise

    # -----------------------------------------
    # LISTAR CLIENTES
    # -----------------------------------------

    def listar_clientes(self):
        """
        Devuelve la lista de clientes registrados.
        """

        return self._clientes.copy()

    # -----------------------------------------
    # LISTAR SERVICIOS
    # -----------------------------------------

    def listar_servicios(self):
        """
        Devuelve la lista de servicios registrados.
        """

        return self._servicios.copy()

    # -----------------------------------------
    # LISTAR RESERVAS
    # -----------------------------------------

    def listar_reservas(self):
        """
        Devuelve la lista de reservas registradas.
        """

        return self._reservas.copy()
