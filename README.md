Sistema de Gestión de Inventario - Inventiendas 📦
Este proyecto corresponde a la evidencia GA7-220501096-AA3-EV01: Codificación de módulos del software. La aplicación es un módulo funcional de inventario que integra lógica de negocio basada en requerimientos previos (Historias de Usuario) y un modelo de datos relacional (Diagrama de Clases).

🚀 Funcionalidades Implementadas
Registro de Productos (HU#1): Captura técnica de nombre, código de barras, categoría, precios y stock inicial.

Alertas de Stock Bajo (HU#3): Sistema de validación lógica que resalta en color rojo los productos que alcanzan el umbral de stock mínimo definido.

Gestión Completa (CRUD):

Lectura: Visualización dinámica desde MySQL.

Actualización: Modales de edición para corregir información del inventario.

Eliminación: Limpieza de registros con confirmación de seguridad.

Interfaz Profesional: Diseño responsivo y amigable para el usuario utilizando Bootstrap 5.

🛠️ Tecnologías Utilizadas
Lenguaje: Python 3.14+

Framework Web: Flask (Microframework).

Base de Datos: MySQL Workbench (Motor relacional).

Versionamiento: Git y GitHub para el control de cambios.

Frontend: Jinja2 Templates, HTML5 y Bootstrap 5.

📋 Requisitos e Instalación
Clonar el repositorio:


git clone https://github.com/Dann-ops/Gutierrez_ADSO_AA3_EV01_Codificacion.git
Instalar dependencias:

pip install flask mysql-connector-python

Configuración de la Base de Datos:

Importar y ejecutar el archivo db_inventiendas.sql en MySQL Workbench para crear la estructura de tablas sincronizada con el diagrama de clases.

Ejecutar la aplicación:

python app.py

📁 Estructura del Proyecto
app.py: Lógica del servidor y rutas del sistema.

templates/index.html: Interfaz de usuario con lógica Jinja2 para alertas.

db_inventiendas.sql: Script de base de datos con datos de prueba.

Historias de usuario.pdf: Documentación de requerimientos.

Diagrama de clases.png: Modelo entidad-relación del sistema.

👤 Autor Dann Esteban Gutierrez Callejas Aprendiz ADSO - SENA

Cali, Valle del Cauca - 2026
