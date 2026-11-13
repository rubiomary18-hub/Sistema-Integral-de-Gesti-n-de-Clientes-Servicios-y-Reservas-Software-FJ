
"""
Archivo: servicios.py

Este módulo define la clase abstracta Servicio y sus tres tipos de servicios especializados.
"""

# Importamos ABC y abstractmethod para crear clases abstractas.
from abc import ABC, abstractmethod

# Importamos la clase Entidad.
from entidades import Entidad

# Importamos nuestra excepción personalizada.
from excepciones import DatosInvalidosError, ErrorCalculoCosto


class Servicio(Entidad, ABC):
    """
    Clase abstracta que representa un servicio general.
    """

    def __init__(self, id_servicio, nombre, precio_base):
        super().__init__(id_servicio)

        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError( "El nombre del servicio no puede estar vacío.")

        if (isinstance(precio_base, bool) or not isinstance(precio_base, (int, float)) or not math.isfinite(precio_base) or precio_base <= 0):
            raise DatosInvalidosError("El precio base debe ser un número mayor que cero.")

        self._nombre = nombre.strip()
        self._precio_base = float(precio_base)

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio_base(self):
        return self._precio_base

    def _validar_cantidad(self, cantidad):
        """
        Comprueba que la cantidad sea un número positivo.
        """
        if ( isinstance(cantidad, bool)or not isinstance(cantidad, (int, float))or cantidad <= 0):
            raise DatosInvalidosError("La cantidad debe ser un número mayor que cero." )

    @abstractmethod
    def validar_parametros(self, cantidad):
        """Valida los parámetros particulares de cada servicio."""
        pass

    @abstractmethod
    def calcular_costo(self, cantidad):
        """Calcula el costo según el tipo de servicio."""
        pass

    @abstractmethod
    def describir_servicio(self):
        """Devuelve una descripción del servicio."""
        pass


# --------------------------------------------------
# SERVICIO 1: RESERVA DE SALAS
# --------------------------------------------------

class ReservaSala(Servicio):
    """
    Servicio para reservar salas por horas.
    """

    def __init__(self, id_servicio, nombre, precio_base, capacidad):
        super().__init__(id_servicio, nombre, precio_base)

        if (isinstance(capacidad, bool)or not isinstance(capacidad, int) or capacidad <= 0):
            raise DatosInvalidosError("La capacidad de la sala debe ser un entero positivo.")

        self._capacidad = capacidad

    def validar_parametros(self, cantidad):
        self._validar_cantidad(cantidad)

    def calcular_costo(self, cantidad):
        self.validar_parametros(cantidad)

        try:
            return self.precio_base * cantidad
        except (TypeError, ValueError) as error:
            raise ErrorCalculoCosto("No fue posible calcular el costo de la reserva de sala.") from error

    def describir_servicio(self):
        return (f"Reserva de sala: {self.nombre}. "f"Capacidad: {self._capacidad} personas. "f"Tarifa por hora: ${self.precio_base:,.2f}." )

    def mostrar_informacion(self):
        return (f"ID: {self.id_entidad}\n" f"{self.describir_servicio()}")


# --------------------------------------------------
# SERVICIO 2: ALQUILER DE EQUIPOS
# --------------------------------------------------

class AlquilerEquipo(Servicio):
    """
    Servicio para alquilar equipos por días.
    """

    def __init__(self, id_servicio, nombre, precio_base, tipo_equipo):
        super().__init__(id_servicio, nombre, precio_base)

        if not isinstance(tipo_equipo, str) or not tipo_equipo.strip():
            raise DatosInvalidosError("Debe especificar un tipo de equipo válido.")

        self._tipo_equipo = tipo_equipo.strip()

    def validar_parametros(self, cantidad):
        self._validar_cantidad(cantidad)

    def calcular_costo(self, cantidad):
        self.validar_parametros(cantidad)

        try:
            return self.precio_base * cantidad
        except (TypeError, ValueError) as error:
            raise ErrorCalculoCosto("No fue posible calcular el costo del alquiler de equipo.") from error

    def describir_servicio(self):
        return (f"Alquiler de equipo: {self.nombre}. "f"Tipo de equipo: {self._tipo_equipo}. "f"Tarifa por día: ${self.precio_base:,.2f}.")

    def mostrar_informacion(self):
        return (f"ID: {self.id_entidad}\n"f"{self.describir_servicio()}")


# --------------------------------------------------
# SERVICIO 3: ASESORÍA ESPECIALIZADA
# --------------------------------------------------

class AsesoriaEspecializada(Servicio):
    """
    Servicio de asesoría especializada por horas.
    """

    def __init__(self, id_servicio, nombre, precio_base, especialidad):
        super().__init__(id_servicio, nombre, precio_base)

        if not isinstance(especialidad, str) or not especialidad.strip():
            raise DatosInvalidosError("Debe especificar una especialidad válida.")

        self._especialidad = especialidad.strip()

    def validar_parametros(self, cantidad):
        self._validar_cantidad(cantidad)

    def calcular_costo(self, cantidad):
        self.validar_parametros(cantidad)

        try:
            return self.precio_base * cantidad
        except (TypeError, ValueError) as error:
            raise ErrorCalculoCosto("No fue posible calcular el costo de la asesoría.") from error

    def describir_servicio(self):
        return (f"Asesoría especializada: {self.nombre}. "f"Especialidad: {self._especialidad}. "f"Tarifa por hora: ${self.precio_base:,.2f}.")

    def mostrar_informacion(self):
        return (f"ID: {self.id_entidad}\n"f"{self.describir_servicio()}")
