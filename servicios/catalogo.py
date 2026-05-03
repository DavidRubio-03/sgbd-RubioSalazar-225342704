"""
Módulo que gestiona el catálogo central de la biblioteca.
"""
import json
import os
from typing import Protocol
from datetime import datetime

from modelos.libro import Libro, LibroDigital, LibroFisico
from modelos.usuario import Usuario, Alumno, Profesor, Administrador
from servicios.prestamo import Prestamo

# 1. Definición del Protocolo (Interfaz)
class Buscable(Protocol):
    """Protocolo que obliga a implementar el método buscar."""
    def buscar(self, query: str) -> list:
        pass


# 2. Implementación de la clase Catalogo
class Catalogo:
    """Gestor central del Sistema de Biblioteca Digital."""
    
    def __init__(self):
        # Colecciones requeridas por el profesor
        self.libros: list[Libro] = []
        self.usuarios: dict[str, Usuario] = {} # El email será la clave del diccionario
        self.prestamos: list[Prestamo] = []

    # --- CRUD Libros ---
    def agregar_libro(self, libro: Libro) -> None:
        self.libros.append(libro)

    def eliminar_libro(self, isbn: str) -> bool:
        # Buscamos el libro y lo eliminamos
        for libro in self.libros:
            if libro.isbn == isbn:
                self.libros.remove(libro)
                return True
        return False

    def listar_disponibles(self) -> list[Libro]:
        # ¡COMPRENSIÓN DE LISTA! (Filtra en una sola línea)
        return [libro for libro in self.libros if libro.disponible]

    def buscar(self, query: str) -> list[Libro]:
        """Implementación del protocolo Buscable usando comprensión de listas."""
        query = query.lower()
        return [
            libro for libro in self.libros 
            if query in libro.titulo.lower() or query in libro.autor.lower() or query in libro.isbn
        ]

    # --- Gestión de Usuarios ---
    def registrar_usuario(self, usuario: Usuario) -> None:
        # Guardamos al usuario en el diccionario usando su email como llave
        self.usuarios[usuario.email] = usuario

    # --- Préstamos y Devoluciones ---
    def registrar_prestamo(self, email_usuario: str, isbn_libro: str) -> bool:
        if email_usuario not in self.usuarios:
            raise KeyError("Usuario no encontrado.")
            
        usuario = self.usuarios[email_usuario]
        
        # Buscamos el libro exacto
        libros_encontrados = [l for l in self.libros if l.isbn == isbn_libro]
        if not libros_encontrados:
            raise ValueError("Libro no encontrado en el catálogo.")
            
        libro = libros_encontrados[0]
        
        if not libro.disponible:
            raise ValueError("El libro no está disponible actualmente.")
            
        # Contamos cuántos préstamos activos tiene este usuario
        prestamos_activos_usuario = len([p for p in self.prestamos if p.usuario.email == email_usuario and p.activo])
        
        if not usuario.puede_pedir_prestado(prestamos_activos_usuario):
            raise ValueError(f"El usuario {usuario.nombre} ha alcanzado su límite de préstamos.")
            
        # Si pasa todas las validaciones, creamos el préstamo
        nuevo_prestamo = Prestamo(usuario, libro)
        self.prestamos.append(nuevo_prestamo)
        return True

        # Añadimos email_usuario como parámetro obligatorio
    def procesar_devolucion(self, email_usuario: str, isbn_libro: str) -> float:
        """Devuelve el libro y calcula la multa si aplica."""
        for prestamo in self.prestamos:
            # Ahora verificamos que coincida el ISBN, que esté activo, ¡Y que sea del usuario correcto!
            if prestamo.libro.isbn == isbn_libro and prestamo.usuario.email == email_usuario and prestamo.activo:
                
                dias_prestado = (datetime.now() - prestamo.fecha_prestamo).days
                dias_retraso = max(0, dias_prestado - 7) 
                
                multa = 0.0
                if hasattr(prestamo.usuario, 'calcular_multa') and dias_retraso > 0:
                    multa = prestamo.usuario.calcular_multa(dias_retraso)
                
                prestamo.cerrar(multa)
                return multa
                
        raise ValueError("No se encontró un préstamo activo para ese usuario y ese ISBN.")

    def generar_reporte(self) -> str:
        return f"Catálogo: {len(self.libros)} libros | {len(self.usuarios)} usuarios | {len(self.prestamos)} préstamos registrados."

    # --- Persistencia Básica (JSON) ---
    def guardar_json(self, ruta: str) -> None:
        """Guarda la estructura básica de los datos en un archivo JSON."""
        datos = {
            "libros": [l.to_dict() for l in self.libros],
            "usuarios": [u.to_dict() for u in self.usuarios.values()]
        }
        # Aseguramos que la carpeta exista antes de guardar
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4)

    def cargar_json(self, ruta: str) -> None:
        """Carga los datos y reconstruye los objetos en memoria."""
        if not os.path.exists(ruta):
            raise FileNotFoundError(f"El archivo {ruta} no existe aún.")
            
        with open(ruta, 'r', encoding='utf-8') as f:
            datos = json.load(f)
            
            # Limpiamos las listas para no duplicar datos si cargamos dos veces
            self.libros = []
            self.usuarios = {}
            
            # 1. Reconstruir Libros
            for lib_data in datos.get("libros", []):
                # Para simplificar el proyecto, los recargamos como Libros genéricos
                nuevo_libro = Libro(
                    titulo=lib_data.get('titulo', 'Desconocido'),
                    autor=lib_data.get('autor', 'Desconocido'),
                    isbn=lib_data.get('isbn', '0000000000000'),
                    anio=lib_data.get('anio', 2000),
                    genero=lib_data.get('genero', 'Desconocido')
                )
                nuevo_libro._disponible = lib_data.get('disponible', True)
                self.libros.append(nuevo_libro)
                
            # 2. Reconstruir Usuarios
            for usu_data in datos.get("usuarios", []):
                # Usamos el 'rol' que guardamos en el diccionario para saber qué objeto crear
                if usu_data.get("rol") == "Profesor":
                    usuario = Profesor(usu_data["nombre"], usu_data["email"], "General")
                elif usu_data.get("rol") == "Admin":
                    usuario = Administrador(usu_data["nombre"], usu_data["email"], 1)
                else:
                    usuario = Alumno(usu_data["nombre"], usu_data["email"], "General", 1)
                
                self.usuarios[usuario.email] = usuario
                
            print(f"✅ ¡Datos cargados y reconstruidos desde {ruta}!")

# Pruebas rápidas
if __name__ == "__main__":
    biblioteca = Catalogo()
    print("Catálogo creado con éxito.")
    
    # Creamos un usuario y un libro
    alumno = Alumno("David", "david@correo.com", "Sistemas", 5)
    libro = LibroFisico("Python Pro", "Guido", "9781234567897", 2023, "Tech", "A1", 3)
    
    biblioteca.registrar_usuario(alumno)
    biblioteca.agregar_libro(libro)
    
    print("\n--- Búsqueda ---")
    resultados = biblioteca.buscar("python")
    print(f"Encontrados: {len(resultados)}")
    
    print("\n--- Préstamo ---")
    biblioteca.registrar_prestamo("david@correo.com", "9781234567897")
    print("Préstamo registrado exitosamente.")
    
    print("\n--- Guardando JSON ---")
    biblioteca.guardar_json("datos/biblioteca.json")
    print("Datos guardados en la carpeta 'datos'.")