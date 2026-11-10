
"""
Archivo: excepciones.py
Proyecto: Sistema Integral de Gestión de Clientes,Servicios y Reservas - Software FJ.

Contiene las excepciones que permiten controlar los errores del sistema.
"""
class SistemaError(Exception):
    """Excepción  para los errores propios del sistema."""
    pass

class DatosInvalidosError(SistemaError):
    """Se crea cuando los datos ingresados no son válidos."""
    pass
  
class ClienteNoEncontradoError(SistemaError):
    """Se crea cuando un cliente no está registrado."""
    pass

class ServicioNoDisponibleError(SistemaError):
    """Se crea cuando un servicio no está disponible."""
    pass

class ReservaInvalidaError(SistemaError):
    """Se crea cuando una reserva presenta información incorrecta."""
    pass

class OperacionNoPermitidaError(SistemaError):
    """Se crea cuando se intenta realizar una operación no permitida."""
    pass
  
class ParametroFaltanteError(SistemaError):
    """Se crea cuando falta un parámetro obligatorio."""
    pass

class ErrorCalculoCosto(SistemaError):
    """Se creaa cuando ocurre un error al calcular un costo."""
    pass
