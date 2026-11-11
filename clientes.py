
"""
Archivo: clientes.py
Proyecto: Sistema Integral de Gestión de Clientes,Servicios y Reservas - Software FJ.

Este módulo contiene la clase Cliente, encargada
de registrar y validar la información de los clientes.
"""

# Importamos la clase abstracta Entidad.
from entidades import Entidad

# Importamos la excepción para datos incorrectos.
from excepciones import DatosInvalidosError

# Importamos re para validar el formato del correo y teléfono.
import re


class Cliente(Entidad):
    """
    Clase que representa a un cliente del sistema Software FJ.
    Hereda de Entidad y aplica encapsulamiento y validaciones.
    """

    def __init__(self, id_cliente, nombre, correo, telefono, direccion):
        """
        Inicializa un cliente con sus datos personales.
        """

        # Inicializamos el identificador mediante la clase padre.
        super().__init__(id_cliente)

        # Validamos y asignamos cada dato utilizando sus propiedades.
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion

    # -------------------------------
    # VALIDACIÓN DEL NOMBRE
    # -------------------------------

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):

        if not isinstance(valor, str):
            raise DatosInvalidosError("El nombre del cliente debe ser texto.")

        valor = valor.strip()

        if len(valor) < 3 or not re.fullmatch(
            r"[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s]+", valor):
            raise DatosInvalidosError("El nombre debe tener al menos 3 caracteres ""y contener únicamente letras y espacios.")

        self._nombre = valor

    # -------------------------------
    # VALIDACIÓN DEL CORREO
    # -------------------------------

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):

        if not isinstance(valor, str):
            raise DatosInvalidosError("El correo electrónico debe ser texto.")

        valor = valor.strip().lower()

        patron = r"^[\w.+-]+@[\w-]+\.[A-Za-z]{2,}$"

        if not re.fullmatch(patron, valor):
            raise DatosInvalidosError("El formato del correo electrónico no es válido.)

        self._correo = valor

    # -------------------------------
    # VALIDACIÓN DEL TELÉFONO
    # -------------------------------

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):

        if not isinstance(valor, str):
            raise DatosInvalidosError("El teléfono debe ingresarse como texto.")

        valor = valor.strip()

        # Permitimos números, espacios, guiones y el signo +.
        patron = r"^\+?[0-9\s-]{7,20}$"

        if not re.fullmatch(patron, valor):
            raise DatosInvalidosError("El número telefónico no tiene un formato válido.")

        # Verificamos que contenga entre 7 y 15 dígitos.
        cantidad_digitos = sum(caracter.isdigit() for caracter in valor)

        if not 7 <= cantidad_digitos <= 15:
            raise DatosInvalidosError("El teléfono debe contener entre 7 y 15 dígitos.")

        self._telefono = valor

    # -------------------------------
    # VALIDACIÓN DE LA DIRECCIÓN
    # -------------------------------

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, valor):

        if not isinstance(valor, str):
            raise DatosInvalidosError("La dirección debe ingresarse como texto.")

        valor = valor.strip()

        if len(valor) < 5:
            raise DatosInvalidosError("La dirección debe contener al menos 5 caracteres.)

        self._direccion = valor

    # -------------------------------
    # MÉTODO PARA MOSTRAR INFORMACIÓN
    # -------------------------------

    def mostrar_informacion(self):
        """
        Devuelve la información general del cliente.
        """

        return (f"ID: {self.id_entidad}\n"f"Nombre: {self.nombre}\n"f"Correo: {self.correo}\n"f"Teléfono: {self.telefono}\nf"Dirección: {self.direccion}")
