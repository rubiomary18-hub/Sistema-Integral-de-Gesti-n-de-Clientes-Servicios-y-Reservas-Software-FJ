
"""
Archivo: reservas.py

Este módulo contiene la clase reserva, encargada de administrar las reservas de clientes y servicios.
"""

# Importamos la clase Entidad.
from entidades import Entidad

# Importamos la clase Cliente.
from clientes import Cliente

# Importamos la clase abstracta Servicio.
from servicios import Servicio

# Importamos las excepciones personalizadas.
from excepciones import (DatosInvalidosError,ClienteNoEncontradoError,ServicioNoDisponibleError,ReservaInvalidaError,OperacionNoPermitidaError,ErrorCalculoCosto)

# Importamos math para validar cantidades numéricas.
import math

# Importamos las funciones para registrar eventos y errores.
from registro_logs import registrar_evento, registrar_error

class Reserva(Entidad):
    """
    Clase que representa una reserva dentro del sistema.
    """

    def __init__(self, id_reserva, cliente, servicio, duracion):
        """
        Inicializa una reserva con su cliente, servicio y duración.
        """

        # Inicializamos el identificador mediante la clase padre.
        super().__init__(id_reserva)

        # Comprobamos que el cliente sea un objeto de tipo Cliente.
        if not isinstance(cliente, Cliente):
            raise ClienteNoEncontradoError("No se puede crear la reserva: el cliente no es válido.")

        # Comprobamos que el servicio sea un objeto de tipo Servicio.
        if not isinstance(servicio, Servicio):
            raise ServicioNoDisponibleError("No se puede crear la reserva: el servicio no es válido.")

        # Validamos la duración de la reserva.
        self._validar_duracion(duracion)

        # Guardamos los datos de la reserva.
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = float(duracion)

        # Toda reserva comienza en estado pendiente.
        self._estado = "Pendiente"

        # Inicializamos el costo sin calcular.
        self._costo_total = None

    # -----------------------------------------
    # VALIDACIÓN DE LA DURACIÓN
    # -----------------------------------------

    @staticmethod
    def _validar_duracion(duracion):
        """
        Comprueba que la duración sea un número positivo y válido.
        """

        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)) or not math.isfinite(duracion) or duracion <= 0:
            raise DatosInvalidosError( "La duración debe ser un número positivo y válido.")

    # -----------------------------------------
    # PROPIEDADES DE LA RESERVA
    # -----------------------------------------

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def duracion(self):
        return self._duracion

    @property
    def estado(self):
        return self._estado

    @property
    def costo_total(self):
        return self._costo_total



    # -----------------------------------------
    # CONFIRMAR RESERVA
    # -----------------------------------------

    def confirmar(self):
        """
        Confirma una reserva que se encuentra pendiente.
        """

        try:
            if self._estado != "Pendiente":
                raise OperacionNoPermitidaError("Solamente se pueden confirmar reservas pendientes.")

            self._estado = "Confirmada"
            registrar_evento(f"Reserva {self.id_entidad} confirmada correctamente.")

            return "La reserva ha sido confirmada correctamente."

        except Exception as error:
            registrar_error("Error al confirmar la reserva", error)
            raise

    # -----------------------------------------
    # CANCELAR RESERVA
    # -----------------------------------------

    def cancelar(self):
        """
        Cancela una reserva pendiente o confirmada.
        """

        try:
            if self._estado not in ("Pendiente", "Confirmada"):
                raise OperacionNoPermitidaError("No se puede cancelar una reserva que ya fue procesada o cancelada.")

            self._estado = "Cancelada"
            registrar_evento(f"Reserva {self.id_entidad} cancelada correctamente.")

            return "La reserva ha sido cancelada correctamente."

        except Exception as error:
            registrar_error("Error al cancelar la reserva", error)
            raise

    # -----------------------------------------
    # PROCESAR RESERVA
    # -----------------------------------------

    def procesar(self):
        """
        Procesa una reserva confirmada y calcula su costo.
        """

        try:
            if self._estado != "Confirmada":
                raise OperacionNoPermitidaError("Solamente se pueden procesar reservas confirmadas.")

            try:
                self._costo_total = self._servicio.calcular_costo(self._duracion)
                self._estado = "Procesada"

                registrar_evento(f"Reserva {self.id_entidad} procesada correctamente. Costo total: ${self._costo_total:,.2f}.")

                return self._costo_total

            except (ErrorCalculoCosto, DatosInvalidosError) as error:
                raise ReservaInvalidaError("No fue posible procesar la reserva debido a un error en el cálculo del costo.") from error

        except Exception as error:
            registrar_error(f"Error al procesar la reserva {self.id_entidad}", error)
            raise

    # -----------------------------------------
    # MOSTRAR INFORMACIÓN
    # -----------------------------------------

    def mostrar_informacion(self):
        """
        Devuelve los datos generales de la reserva.
        """

        costo = f"${self._costo_total:,.2f}" if self._costo_total is not None else "Pendiente de cálculo"

        return f"ID de reserva: {self.id_entidad}\nCliente: {self._cliente.nombre}\nServicio: {self._servicio.nombre}\nDuración: {self._duracion}\nEstado: {self._estado}\nCosto total: {costo}"


