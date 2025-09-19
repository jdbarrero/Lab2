**Laboratorio 2: Servidor de Afiliados, Encuestas, Citas y Prescripciones (RA 1, RA 3, RA 4)**
Programación, II-2025
Uniquindío

Con esta práctica se continuará el desarrollo del código fuente en Python del proyecto del espacio académico. En este caso, y de acuerdo con la arquitectura mostrada en la siguiente figura, se construirá el código del lado del servidor para la gestión de **afiliados y encuestas de satisfacción**, y se incorporará un módulo clínico para la gestión de **citas médicas y prescripciones**.

![Presentación / Arquitectura](https://github.com/jdbarrero/Lab2/blob/main/Presentaci%C3%B3n.png)

En ese sentido, la práctica de laboratorio contempla la creación y prueba de funciones que hacen uso de archivos para la gestión de afiliados, encuestas y flujo clínico (usuarios con rol/sesión, citas y prescripciones), así como las demás estructuras de programación y tipos de datos estudiados hasta el momento.

**Código base suministrado**
Se suministra el código base del servidor en el archivo [`eps_server.py`](https://github.com/jdbarrero/Lab2/blob/main/eps_server.py) el cual contiene toda la funcionalidad para que éste opere dentro de una red de área local o en el mismo equipo de prueba. Este archivo no debe ser modificado bajo ninguna circunstancia.

El archivo [`eps_server.py`](https://github.com/jdbarrero/Lab2/blob/main/eps_server.py) usa los módulos [`affiliates.py`](https://github.com/jdbarrero/Lab2/blob/main/affiliates.py) y [`clinical.py`](https://github.com/jdbarrero/Lab2/blob/main/clinical.py), que incluyen definiciones de funciones a implementar de acuerdo con los comentarios en cada archivo. La implementación y el correcto funcionamiento de estas funciones determinan la evaluación de esta práctica de laboratorio y el lado del servidor del proyecto.

![Demostracion](https://github.com/jdbarrero/Lab2/blob/main/Demostracion.png)

El servidor permite:

* **Afiliados y encuestas**

  * Registrar afiliados con sus datos.
  * Listar afiliados y buscar por ID.
  * Consultar estadísticas (totales por plan, promedios de edad por género, edad mínima y máxima).
  * Registrar encuestas de satisfacción (rating 1..5) y consultar estadísticas globales o segmentadas.
  * Exportar/asegurar los archivos CSV requeridos.
* **Usuarios con sesión y roles** (`patient`, `doctor`, `administrativo`).
* **Citas y prescripciones**

  * Agendar, listar y cancelar citas (validaciones: lunes a viernes, 08:00–16:00, intervalos de 30 minutos; evitar colisión del mismo médico en el mismo horario).
  * Crear prescripciones asociadas a una cita y listarlas según el rol (el paciente ve las suyas; el doctor ve las que emitió).

También se suministran el cliente y dos pruebas de ejemplo:

* Cliente (no modificar): [`eps_client.py`](https://github.com/jdbarrero/Lab2/blob/main/eps_client.py)
* Pruebas (pueden modificarse por el equipo):

  * [`test_client.py`](https://github.com/jdbarrero/Lab2/blob/main/test_client.py) – flujo de **usuarios + afiliados + encuestas**.
  * [`test_medical_client.py`](https://github.com/jdbarrero/Lab2/blob/main/test_medical_client.py) – flujo **paciente–doctor → cita → prescripción**.

Para que [`eps_client.py`](https://github.com/jdbarrero/Lab2/blob/main/eps_client.py) pueda funcionar correctamente se debe instalar la librería de solicitudes de Python ejecutando el siguiente comando en una terminal:
`python -m pip install requests`

**¿Cómo realizar las pruebas?**
Primero ejecute el programa  [`eps_server.py`](https://github.com/jdbarrero/Lab2/blob/main/eps_server.py) ; la recomendación es verificar el correcto funcionamiento de las funciones, una a la vez. Posteriormente se pueden ejecutar los programas `test_client.py` y `test_medical_client.py`; en caso de que se muestren ventanas emergentes de Windows solicitando permisos, por favor otorgarlos ya que los programas hacen uso de los servicios de red.

Tenga en cuenta que es posible que [`eps_server.py`](https://github.com/jdbarrero/Lab2/blob/main/eps_server.py), [`test_client.py`](https://github.com/jdbarrero/Lab2/blob/main/test_client.py) y [`test_medical_client.py`](https://github.com/jdbarrero/Lab2/blob/main/test_medical_client.py) se ejecuten en computadoras diferentes siempre y cuando los equipos se encuentren conectados a la misma red LAN cableada o inalámbrica. En ese caso basta con consultar la dirección IP del computador que está ejecutando ** [`eps_server.py`](https://github.com/jdbarrero/Lab2/blob/main/eps_server.py) ** mediante el comando `ipconfig`, como se muestra en la siguiente figura:

![Configurar IP](https://github.com/jdbarrero/Lab2/blob/main/CONFIG.png)

La IP encontrada debe sustituir `localhost` en los archivos de prueba en la línea donde se define la URL base del servidor.

Para esta práctica, el/la estudiante **solo debe modificar** [`affiliates.py`](https://github.com/jdbarrero/Lab2/blob/main/affiliates.py) y [`clinical.py`](https://github.com/jdbarrero/Lab2/blob/main/clinical.py) (implementando las funciones solicitadas con parámetros explícitos). **Cambios en** [`eps_server.py`](https://github.com/jdbarrero/Lab2/blob/main/eps_server.py) **o** [`eps_client.py`](https://github.com/jdbarrero/Lab2/blob/main/eps_client.py) **no están permitidos**.

**Entrega del laboratorio**
El laboratorio debe ser presentado mediante:

1. Repositorio en GitHub.
2. Informe de laboratorio.
   El informe de laboratorio y el enlace al repositorio de GitHub deben ser compartidos en el enlace dispuesto para tal fin en la plataforma Google Classroom.
