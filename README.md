
# Sistema Integral de Gestión de Clientes, Servicios y Reservas - Software FJ

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un sistema integral de gestión de clientes, servicios y reservas para la empresa Software FJ, utilizando el lenguaje de programación Python.

El sistema permite registrar y administrar clientes, gestionar diferentes tipos de servicios y crear, confirmar, cancelar y procesar reservas.

## Objetivo

Implementar una solución basada en programación orientada a objetos que permita administrar la información mediante clases, objetos, validaciones y manejo de excepciones, garantizando una gestión organizada y robusta de las operaciones.

## Funcionalidades principales

- Registro y validación de clientes.
- Administración de servicios especializados.
- Gestión de reservas.
- Confirmación, cancelación y procesamiento de reservas.
- Cálculo de costos de los servicios.
- Búsqueda de clientes y servicios.
- Manejo de excepciones personalizadas.
- Registro de eventos y errores en archivos de log.

## Conceptos de programación utilizados

- Programación orientada a objetos.
- Abstracción.
- Herencia.
- Polimorfismo.
- Encapsulamiento.
- Clases abstractas.
- Validación de datos.
- Manejo avanzado de excepciones.
- Registro de eventos y errores.

## Estructura del proyecto

- `main.py`: ejecuta el programa y las operaciones de prueba.
- `entidades.py`: contiene la clase abstracta Entidad.
- `clientes.py`: administra los datos y validaciones de los clientes.
- `servicios.py`: contiene la clase abstracta Servicio y los servicios especializados.
- `reservas.py`: administra las reservas de clientes y servicios.
- `excepciones.py`: define las excepciones personalizadas.
- `registro_logs.py`: configura el registro de eventos y errores.
- `sistema.py`: integra y administra las operaciones del sistema.

## Ejecución del programa

Para ejecutar el sistema, se debe contar con Python instalado y ejecutar el archivo principal:

```bash
python main.py
```

Los registros de eventos y errores se almacenan automáticamente en la carpeta `logs`, dentro del archivo `sistema.log`.


