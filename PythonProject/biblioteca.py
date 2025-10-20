class Libro:
    def __init__(self, titulo, autor, año_publicacion, idlibro):
        self.titulo: str = titulo
        self.autor: str = autor
        self.año_publicacion: int = año_publicacion
        self.prestado : bool = False
        self.id: int = idlibro
    def mostrar_info(self):
        prestado_msg = "Si" if self.prestado else "No"
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicacion: {self.año_publicacion}")
        print(f"Prestado: {prestado_msg}")
        print(f"ID: {self.id}")
        print("")
    def prestar(self):
        if not self.prestado:
            self.prestado = True
            print("Libro prestado exitosamente")
        else:
            print("El libro ya había sido prestado")
    def devolver(self):
        if not self.prestado:
            print("El libro no había sido prestado")
        else:
            print("Libro recibido")

def agregar_libro(biblioteca, titulo, autor, año):
    idlibro = len(biblioteca)
    biblioteca.append(Libro(titulo, autor, año, idlibro))

def listar_disponibles(biblioteca):
    print("Listado de libros disponibles:\n")
    for libro in biblioteca:
        if not libro.prestado:
            libro.mostrar_info()

def buscar_por_autor(biblioteca, autor):
    print(f"Libros del autor {autor}: \n")
    for libro in biblioteca:
        if libro.autor == autor:
            libro.mostrar_info()

def libro_mas_antiguo(biblioteca):
    libro_antiguo = biblioteca[0]
    menor_año = biblioteca[0].año_publicacion

    for libro in biblioteca:
        if libro.año_publicacion<menor_año:
            menor_año=libro.año_publicacion
            libro_antiguo = libro
    print("Libro mas antiguo: \n")
    libro_antiguo.mostrar_info()
def prestar_libro(biblioteca, id):
    if id > len(biblioteca):
        print("ID invalida")
        return

    for libro in biblioteca:
        if (libro.id == id) and (libro.prestado):
            print(f"El libro {libro.titulo} ya ha sido prestado por alguien más")
        elif libro.id == id:
            libro.prestado = True
            print(f"Libro {libro.titulo} prestado exitosamente")
def main():
    biblioteca = []
    agregar_libro(biblioteca,"Cien años de soledad", "Gabriel García Márquez", 1967)
    agregar_libro(biblioteca,"Don Quijote", "Miguel de Cervantes", 1605)
    agregar_libro(biblioteca,"El principito", "Antoine de Saint-Exupéry", 1943)
    agregar_libro(biblioteca,"1984", "George Orwell", 1949)
    agregar_libro(biblioteca,"Rayuela", "Julio Cortázar", 1963)
    listar_disponibles(biblioteca)
    prestar_libro(biblioteca, 6)
    prestar_libro(biblioteca,0)
    prestar_libro(biblioteca,1)
    prestar_libro(biblioteca,1)
    listar_disponibles(biblioteca)
    buscar_por_autor(biblioteca,"George Orwell")
    libro_mas_antiguo(biblioteca)
main()