# 🛒 Proyecto de Pruebas API - URBAN GROCERS

## 🚀 Descripción

Este proyecto automatiza pruebas para la API de **Urban Grocers**, una aplicación que permite gestionar kits personalizados.  
Las pruebas están enfocadas en validar la creación de kits a través del endpoint correspondiente, específicamente verificando diferentes casos para el campo `name` en el request.

El objetivo principal es asegurar que la API responda correctamente ante distintas entradas, incluyendo:

- Validaciones de longitud mínima y máxima.
- Inclusión de caracteres especiales.
- Ausencia del campo `name`.
- Tipos de datos incorrectos.

## 📚 Fuente de documentación

La documentación de la API fue consultada a través de **apiDoc**, disponible en:  
https://cnt-101beed5-59ed-4630-a31b-512ed1ea1f59.containerhub.tripleten-services.com/docs/

## 🧪 Tecnologías y técnicas utilizadas

- **Python 3.x**
- **Pytest** para la ejecución de pruebas automatizadas.
- **Requests** para realizar peticiones HTTP a la API.
- **Programación modular**: el proyecto se divide en archivos reutilizables como `configuration.py`, `data.py`, y `sender_stand_request.py`.
- **Buenas prácticas en pruebas automatizadas**, como separación entre pruebas positivas y negativas.

## ⚙️ Requisitos previos

Antes de ejecutar el proyecto, asegúrate de contar con lo siguiente:

- Python 3.x instalado.
- Acceso a una terminal o consola.
- PyCharm o cualquier editor de código.
- Git configurado (opcional, si vas a cargarlo en GitHub).

## 📦 Instalación de librerías

Para instalar las dependencias necesarias, ejecuta:

```bash
pip install requests
pip install pytest
📁 Estructura del proyecto
bash
Copiar
Editar
qa-project-Urban-Grocers-app-es/
├── configuration.py             # Configuración de URL y endpoints
├── data.py                      # Datos y headers para las peticiones
├── sender_stand_request.py      # Funciones para llamadas a la API
└── create_kit_name_kit_test.py  # Pruebas automatizadas con pytest


## ▶️ ¿Cómo ejecutar las pruebas?

1. Abre una terminal y navega a la carpeta raíz del proyecto. Por ejemplo:

```bash
cd C:/Users/sarac/projects/qa-project-Urban-Grocers-app-es
Asegúrate de tener instalado pytest. Si no lo tienes, puedes instalarlo con:

bash
Copiar
Editar
pip install pytest

2. Para ejecutar todas las pruebas del proyecto, usa el siguiente comando:

bash
Copiar
Editar
pytest .

Esto buscará automáticamente todos los archivos de prueba (test_*.py o *_test.py) en el directorio actual y subdirectorios.

3. Si deseas ejecutar solo un archivo específico, por ejemplo create_kit_name_kit_test.py, usa:

bash
Copiar
Editar
pytest create_kit_name_kit_test.py

4. Para ver una salida más detallada de los resultados, puedes agregar el flag -v (verbose):

bash
Copiar
Editar
pytest -v
