### Prompt #1
**Tarea:** 1.1 Configuración y 1.2 Variables
**LLM usada:** Gemini
**Fecha/Hora:** 2026-05-01 12:00
**Prompt enviado:** Ayúdame a crear la estructura de carpetas del proyecto, configurar Git, crear las constantes en SCREAMING_SNAKE_CASE y las funciones validar_isbn13 y validar_email.
**Respuesta recibida (resumen):** La IA me dio los comandos de terminal para Git, la estructura de carpetas y el código Python con buenas prácticas y docstrings para las constantes y validaciones.
**Código adoptado o modificado:** Usé el código tal como lo generó la IA, aplicando mis datos personales en la estructura local y de GitHub.
**Lo que aprendí / Lo que la IA no entendió:** Aprendí a inicializar un repositorio en Git y a estructurar un proyecto en Python. La IA entendió bien el contexto y el PDF.
**Temas de la materia que aplica este prompt:** Entorno de desarrollo, Repositorios de código, Palabras reservadas, Identificadores, Operadores.
### Prompt #2
**Tarea:** 1.3 Operadores y sentencias de control
**LLM usada:** Gemini
**Fecha/Hora:** 2026-05-01 12:45
**Prompt enviado:** Ayúdame a crear la función de cálculo de multas usando if/elif/else y match/case. Además, al intentar ejecutar el código obtuve el error: `ModuleNotFoundError: No module named 'utils'`. ¿Cómo lo soluciono?
**Respuesta recibida (resumen):** La IA proporcionó el código usando ambas estructuras de control (if y match). Explicó que el error de módulo ocurre por ejecutar el archivo directamente desde la subcarpeta, y me enseñó a ejecutarlo como módulo desde la raíz usando el comando `python -m`.
**Código adoptado o modificado:** Adopté el código sugerido. Tuve un segundo error (`ImportError`) que solucioné guardando correctamente los archivos (`Ctrl + S`) antes de volver a correr el comando en la terminal.
**Lo que aprendí / Lo que la IA no entendió:** Aprendí a usar la nueva estructura `match/case` de Python 3.10. Lo más valioso fue entender cómo Python maneja las rutas de los archivos y la importancia de ejecutar scripts secundarios como módulos usando la bandera `-m` en la terminal.
**Temas de la materia que aplica este prompt:** Operadores, Sentencias de control (if/elif/else, match/case), Resolución de errores (Debugging).
### Prompt #3
**Tarea:** 1.4 Manejo de Strings
**LLM usada:** Gemini
**Fecha/Hora:** 2026-05-01 13:00
**Prompt enviado:** Ayúdame a crear las funciones de manipulación de strings en utils/formato_texto.py. Necesito normalizar títulos, generar slugs sin acentos usando unicodedata, formatear un reporte con f-strings y hacer búsquedas case-insensitive.
**Respuesta recibida (resumen):** La IA me dio el código completo utilizando expresiones regulares (`re`), `unicodedata` y métodos de string nativos como `strip`, `split`, `join`, `lower` y `title`. 
**Código adoptado o modificado:** Adopté el código y lo ejecuté exitosamente comprobando que la salida en terminal fuera la correcta.
**Lo que aprendí / Lo que la IA no entendió:** Aprendí lo útiles que son las expresiones regulares para limpiar texto y cómo usar f-strings para darle un formato de tabla o reporte visualmente atractivo a un diccionario.
**Temas de la materia que aplica este prompt:** Manejo de Strings, Operadores, Identificadores.