
"""
Archivo: registro_logs.py
Proyecto: Sistema Integral de Gestión de Clientes,Servicios y Reservas - Software FJ.

Este módulo permite registrar los eventos y errores
que ocurren durante la ejecución del sistema.
"""

# Importamos logging para administrar los registros.
import logging

# Importamos os para crear y administrar directorios.
import os


# -----------------------------------------
# CONFIGURACIÓN DEL REGISTRO
# -----------------------------------------

# Definimos el directorio donde se guardarán los registros.
DIRECTORIO_LOGS = "logs"

# Definimos la ruta del archivo de registro.
ARCHIVO_LOGS = os.path.join(DIRECTORIO_LOGS, "sistema.log")

# Creamos el directorio si todavía no existe.
os.makedirs(DIRECTORIO_LOGS, exist_ok=True)


# -----------------------------------------
# CONFIGURACIÓN DEL LOGGER
# -----------------------------------------

# Creamos un registrador para el sistema Software FJ.
logger = logging.getLogger("SoftwareFJ")

# Establecemos el nivel mínimo de registro.
logger.setLevel(logging.INFO)

# Evitamos que los mensajes se repitan en otros registradores.
logger.propagate = False

# Configuramos el archivo de registro si no existe un controlador.
if not logger.handlers:

    # Creamos un controlador para escribir en el archivo.
    manejador = logging.FileHandler(ARCHIVO_LOGS, encoding="utf-8")

    # Definimos el formato de cada registro.
    formato = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s")

    # Aplicamos el formato al controlador.
    manejador.setFormatter(formato)

    # Conectamos el controlador con el registrador.
    logger.addHandler(manejador)


# -----------------------------------------
# REGISTRAR EVENTOS
# -----------------------------------------

def registrar_evento(mensaje):
    """
    Registra los eventos importantes del sistema.
    """

    logger.info(mensaje)


# -----------------------------------------
# REGISTRAR ERRORES
# -----------------------------------------

def registrar_error(mensaje, error=None):
    """
    Registra los errores que ocurren durante las operaciones.
    """

    if error is not None:
        logger.error(f"{mensaje}: {error}",exc_info=(type(error), error, error.__traceback__))
    else:
        logger.error(mensaje)
