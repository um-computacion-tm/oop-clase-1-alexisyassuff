import unittest
  
  
  
class Materia:
    def __init__(self, nombre, profesores, alumnos):
        self.__nombre__ = nombre
        self.__profesores__ = profesores
        self.__alumnos__ = alumnos

    def obtener_profesores(self):
        return self.__profesores__

    def cambiar_nombre(self, nombre):
        self.__nombre__ = nombre
    
    def obtener_alumnos(self):
        return self.__alumnos__


class Profesor:
    def __init__(self, nombre, cargo, legajo):
        self.__nombre__ = nombre
        self.__cargo__ = cargo
        self.__legajo__ = legajo

    def obtener_nombre(self):
        return self.__nombre__

    def obtener_cargo(self):
        return self.__cargo__

    def obtener_legajo(self):
        return self.__legajo__

class Alumno:
    def __init__(self, nombre, edad, legajo):
        self.__nombre__ = nombre
        self.__edad__ = edad
        self.__legajo__ = legajo


        
class Test(unittest.TestCase):
    
    #MATERIA
    def test_materia_init_nombre(self):
        materia = Materia(nombre="Computacion I", profesores="Elio, Dario", alumnos="Juanci, Rita, Jonas")
        self.assertEqual(materia.__nombre__, "Computacion I" )

    def test_materia_init_profesores(self):
        materia = Materia(nombre="Computacion I", profesores="Elio, Dario", alumnos="Juanci, Rita, Jonas")
        self.assertEqual(materia.__profesores__, "Elio, Dario" )
    
    def test_materia_init_alumnos(self):
        materia = Materia(nombre="Computacion I", profesores="Elio, Dario", alumnos="Juanci, Rita, Jonas")
        self.assertEqual(materia.__alumnos__, "Juanci, Rita, Jonas" )
    
    def test_materia_cambiar_nombre(self):
        materia = Materia(nombre="Computacion I", profesores="Elio, Dario", alumnos="Juanci, Rita, Jonas")
        materia.cambiar_nombre(nombre="Ciencia de las computadoras")
        self.assertEqual(materia.__nombre__, "Ciencia de las computadoras")
        
    def test_materia_obtener_profesores(self):
        materia = Materia(nombre="Computacion I", profesores="Elio, Dario", alumnos="Juanci, Rita, Jonas")
        materia.obtener_profesores
        self.assertEqual(materia.__profesores__, "Elio, Dario")
    
    def test_materia_obtener_alumnos(self):
        materia = Materia(nombre="Computacion I", profesores="Elio, Dario", alumnos="Juanci, Rita, Jonas")
        materia.obtener_alumnos
        self.assertEqual(materia.__alumnos__, "Juanci, Rita, Jonas")
    
#ALUMNOS
    def test_inicio_datos_alumno(self):
        alumno = Alumno(nombre="Alexis", edad="20", legajo="62072")
        self.assertEqual(alumno.__nombre__, "Alexis")  
        self.assertEqual(alumno.__edad__, "20")
        self.assertEqual(alumno.__legajo__, "62072")

#PROFESOR

    def test_inicio_datos_profesor(self):
        profesor = Profesor(nombre="Daniel", cargo="Titular", legajo="6363")
        self.assertEqual(profesor.__nombre__, "Daniel")
        self.assertEqual(profesor.__cargo__, "Titular")
        self.assertEqual(profesor.__legajo__, "6363")
    
    def test_obtener_cargo_profesor(self):
        profesor = Profesor(nombre="Daniel", cargo="Titular", legajo="6363")
        profesor.obtener_cargo
        self.assertEqual(profesor.__cargo__, "Titular" )
  
    def test_obtener_nombre_profesor(self):
        profesor = Profesor(nombre="Daniel", cargo="Titular", legajo="6363")
        profesor.obtener_nombre
        self.assertEqual(profesor.__nombre__, "Daniel" )  
    
    def test_obtener_legajo_profesor(self):
        profesor = Profesor(nombre="Daniel", cargo="Titular", legajo="6363")
        profesor.obtener_legajo
        self.assertEqual(profesor.__legajo__, "6363" )
        
        
unittest.main()