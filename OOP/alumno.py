class Alumno:

    def inicializar(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota

    def imprimir(self):
        print("Nombre: ", self._nombre)
        print("Nota: ", self._nota)

    def resultado(self):
        if self._nota < 5:
            print("Estado : Suspendido")
            print("-----------------------------------")
        else:
            print("Estado : Aprobado")
            print("-----------------------------------")


