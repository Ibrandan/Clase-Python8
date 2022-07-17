class Person:
    #  Init es el metodo constructor de la clase, define como construir cada objeto. Siempre recibe el argumento self
    # Self es lo mismo que this en Js, refiere al propio objeto
    def __init__(self, name, age):
        self.name = name    # ---> Variables de instancia
        self.age = age          # --->  Variables de instancia

    def __str__(self):  # Otro metodo, retorna la representacion en string de la clase
        # Para acceder a las variables de instancia usamos el self.
        return "Hola soy {} y tengo {} años".format(self.name, self.age)


# Construccion de un nuevo objeto de la clase person, Dentro de los parentesis, se declaran los argumentos que recibe la clase, en este caso nombre y edad
persona1 = Person("Ignacio", 18)
persona2 = Person("Lionel", 35)
print(persona1)  # --> persona1.__str__()

# Todas las clases se heredan de la clase object ---> class Person(object):


class Student(Person):
    universidad = "ITBA"  # Variable de clase

    def __init__(self, name, age, legajo):
        # self esta como parametro implicito (self, name, age)
        super().__init__(name, age)
        # Suoer llama al constructor de la clase padre, luego se podrian ingresar variables para la clase hijo
        self.legajo = legajo

    def __str__(self):
        # super().__str__() llama al constructor de string de la clase padre y se le concatena "y mi legajo es : {}".format(self.legajo) de la clase hijo
        return super().__str__() + "y mi legajo es : {}".format(self.legajo)


estudiante1 = Student("Ignacio", 18, "94814")
estudiante2 = Student("Sergio", 34, "9814")
print(estudiante1)

# Acceder a las variables de instancia
print(estudiante1.legajo)
print(estudiante1.age)

# Variables de clase
print(estudiante1.universidad)
print(Student.universidad)  # Llama a la clase


class Modifiers:

    def __init__(self, name):
        self.__public_member = name  # Privado


mod = Modifiers("SKAUL05")
# print(mod.__public_member)
mod.__public_member = "GitHub"
# print(mod.__public_member)

class Modifiers:

    def __init__(self, name):
        self.public_member = name  # Publico


mod = Modifiers("SKAUL05")
print(mod.public_member)
mod.public_member = "GitHub"
print(mod.public_member)
