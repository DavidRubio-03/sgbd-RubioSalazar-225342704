# Sistema de Gestión de Biblioteca Digital 📚 (GUI Version)

Este proyecto es la evaluación práctica del Módulo de Programación Orientada a Objetos en Python. Consiste en un sistema completo de gestión de biblioteca con una **Interfaz Gráfica de Usuario (GUI) responsiva**, persistencia de datos y manejo de reglas de negocio.

## Características Principales
* **Interfaz Gráfica (Tkinter):** Diseño amigable, menús desplegables, tablas de auditoría y prevención de errores mediante validación visual.
* **Gestión de Catálogo y Usuarios:** Registro de libros físicos/digitales y usuarios (Alumnos, Profesores, Admins) aplicando herencia y polimorfismo.
* **Sistema de Préstamos y Multas:** Lógica estricta de control de stock (ejemplares) y cálculo automatizado de días de retraso.
* **Cola de Espera (FIFO):** Sistema automatizado (`collections.deque`) para asignar libros apartados en cuanto son devueltos.
* **Persistencia Robusta:** Guardado y deserialización segura de objetos usando archivos `.json`, manteniendo el estado de los préstamos incluso al cerrar la aplicación.

## Tecnologías Utilizadas
* Python 3.10+
* Tkinter (GUI Nativa)
* Módulo `abc` (Clases Abstractas)
* Pytest (Pruebas Unitarias Automatizadas)
* JSON (Persistencia de Datos)

## Cómo ejecutar el proyecto
1. Clona o descarga este repositorio.
2. Abre una terminal en la raíz de la carpeta del proyecto.
3. **Para abrir la Interfaz Gráfica (Punto de entrada principal):** Ejecuta el comando `python MiExamen.py`
4. *(Opcional)* Para verificar las pruebas unitarias de los validadores, ejecuta: `python -m pytest`
