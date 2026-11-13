
"""
Archivo: Entidades.py

Este módulo define la clase abstracta Entidad,que sirve como estructura general para las clases que representan elementos del sistema.
"""

# Importamos ABC y abstractmethod para crear clases abstractas.
from abc import ABC, abstractmethod

# Importamos nuestra excepción personalizada.
from excepciones import DatosInvalidosError


class Entidad(ABC):
    """
    Clase abstracta que representa una entidad general dentro del sistema Software FJ.
    """

    def __init__(self, id_entidad):
        """
        Inicializa una entidad con un identificador único.
        """

        # Validamos que el identificador sea texto o número entero.
        if isinstance(id_entidad, bool) or not isinstance(id_entidad, (str, int)):
            raise DatosInvalidosError("El identificador debe ser un texto o un número entero.")

        # Convertimos el identificador a texto y eliminamos espacios.
        self._id_entidad = str(id_entidad).strip()

        # Comprobamos que el identificador no esté vacío.
        if not self._id_entidad:
            raise DatosInvalidosError("El identificador de la entidad no puede estar vacío.")

    @property
    def id_entidad(self):
        """
        Permite consultar el identificador de la entidad sin modificarlo directamente.
        """
        return self._id_entidad

    @abstractmethod
    def mostrar_informacion(self):
        """
        Método abstracto que deberán implementar las clases que hereden de Entidad.
        """
        pass
