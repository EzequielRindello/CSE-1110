import alumno as alm


def main():
    print("-----------------------------------")
    # Creamos alumnos y los inicializamos.
    alumno1 = alm.Alumno()
    alumno1.inicializar("Juan", 8)
    alumno1.imprimir()
    alumno1.resultado()

    alumno2 = alm.Alumno()
    alumno2.inicializar("Pedro", 3)
    alumno2.imprimir()
    alumno2.resultado()
    
    alumno3 = alm.Alumno()
    alumno3.inicializar("Maria", 9)
    alumno3.imprimir()
    alumno3.resultado()


if __name__ == "__main__":
    main()
