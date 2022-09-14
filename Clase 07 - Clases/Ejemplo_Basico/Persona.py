class Persona:
    # Constructor de la clase con sus atributos
    def __init__(self, name, age, gender, residence):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__residence = residence

    # Geters
    # Decorador property (Para que lo reconozca como propiedad y no como método)
    @property
    def name (self):
        return self.__name

    @property
    def age (self):
        return self.__age

    @property
    def gender (self):
        return self.__gender

    @property
    def residence (self):
        return self.__residence


    # Setters
    # Decorador setter (Para que lo reconozca como setter y no como método)
    @name.setter
    def name (self, name):
        self.__name = name

    @age.setter
    def age (self, age):
        self.__age = age
    
    @gender.setter
    def gender (self, gender):
        self.__gender = gender

    @residence.setter
    def residence (self, residence):
        self.__residence = residence
    

    # Métodos
    def comer (self):
        return 'Soy ' + self.__name + ' y estoy comiendo'

    def caminar (self):
        return 'Soy ' + self.__name + ' y estoy caminando'
    
