**Laboratorio 2: Servidor de Afiliados y Encuestas (RA 1, RA 3, RA4)**   
Programación, II-2025  
Uniquindío

Con esta práctica se iniciará el desarrollo del código fuente en Python del proyecto del espacio académico. En este caso, y de acuerdo con la arquitectura mostrada en la siguiente figura, se construirá el código del lado del servidor para la gestión de afiliados y encuestas de satisfacción.

![Presentación / Arquitectura](https://github.com/jdbarrero/Lab2/blob/main/Presentaci%C3%B3n.png)

En ese sentido, la práctica de laboratorio contempla la creación y prueba de funciones que hacen uso de archivos para la gestión de los afiliados y las encuestas, así como las demás estructuras de programación y tipos de datos estudiados hasta el momento.

**Código base suministrado**  
Se suministra el código base del servidor en el archivo [`eps_server.py`](https://github.com/jdbarrero/Lab2/blob/main/eps_server.py) el cual contiene toda la funcionalidad para que éste opere dentro de una red de área local o en el mismo equipo de prueba. Este archivo no debe ser modificado bajo ninguna circunstancia.

En ese sentido, el archivo `eps_server.py` usa el archivo [`affiliates.py`](https://github.com/jdbarrero/Lab2/blob/main/affiliates.py) que incluye definiciones de funciones las cuales deben ser implementadas en el laboratorio de acuerdo a lo descrito en los comentarios del archivo. La implementación de estas funciones y su correcto funcionamiento determina la evaluación de esta práctica de laboratorio y el lado del servidor del proyecto.

El servidor permite registrar afiliados con sus datos y, una vez registrados, se podrá:
- Listar afiliados y buscar por ID.  
- Actualizar y consultar estadísticas (totales por plan, promedios de edad por género, edad mínima y máxima).  
- Registrar encuestas de satisfacción (rating 1..5) y consultar estadísticas globales o segmentadas.  
- Exportar/asegurar los archivos CSV requeridos.

También, se suministran los archivos [`eps_client.py`](https://github.com/jdbarrero/Lab2/blob/main/eps_client.py) y [`test_eps_client.py`](https://github.com/jdbarrero/Lab2/blob/main/test_eps_client.py). En este caso, `eps_client.py` implementa la funcionalidad básica de los clientes para la conexión con el servidor por lo que no debe ser modificado bajo ninguna circunstancia. De otro lado, `test_eps_client.py` es un archivo de prueba que se suministra para verificar el correcto funcionamiento del servidor y que puede ser modificado a gusto de los miembros del equipo. Para que `eps_client.py` pueda funcionar correctamente se debe instalar el módulo de solicitudes de Python ejecutando el siguiente comando en una terminal:

`python -m pip install requests`

**¿Cómo realizar las pruebas?**  
Para la realización de las pruebas debe ejecutar primero el programa `eps_server.py`; la recomendación es verificar el correcto funcionamiento de las funciones, una a la vez. Posteriormente se puede ejecutar el programa `test_eps_client.py`; en caso de que se muestren ventanas emergentes de Windows solicitando permisos, por favor otorgarlos ya que los programas hacen uso de los servicios de red.

Tenga en cuenta que es posible que `eps_server.py` y `test_eps_client.py` se ejecuten en computadoras diferentes siempre y cuando los equipos se encuentren conectados a la misma red LAN cableada o inalámbrica. En ese caso basta con consultar la dirección IP del computador que está ejecutando `eps_server.py` mediante el comando `ipconfig`, como se muestra en la siguiente figura:

![Configurar IP](https://github.com/jdbarrero/Lab2/blob/main/CONFIG.png)

La IP encontrada debe sustituir `localhost` en el archivo `test_eps_client.py` en la línea donde se define la URL base del servidor.

Para esta práctica, el/la estudiante solo debe modificar affiliates.py (implementando las funciones solicitadas con parámetros explícitos). Cambios en eps_server.py o eps_client.py no están permitidos.  
**Entrega del laboratorio**  
El laboratorio debe ser presentado mediante:  
1. Repositorio en GitHub.  
2. Informe de laboratorio.  
El informe de laboratorio y el enlace al repositorio de GitHub deben ser compartidos en el enlace dispuesto para tal fin en la plataforma Google Classroom.
