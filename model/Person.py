class Person:
    def __init__(self, name:str, age:float | int, weight:float | int, height:int):
        # Properties
        self.__name:str = name
        self.__age:float = age # 0.0 hasta 0.12 Son meses, > son años
        self.__weight:float = weight
        self.__height:int = height
        # Actions
        self.__walking:bool = False
        self.__speaking:bool = False
        self.__running:bool = False
    
    def __str__(self) -> str:
        return f'Nombre: {self.__name}\nEdad: {self.__format_age()}\nPeso: {self.__weight} Kg\nAltura: {self.__height} CM\n'

    def walk(self) -> None:
        """Cambia el estado de la persona a camninar
        """
        self.__walking = True

    def speak(self, message:str) -> None:
        """Hace que la persona hable

        Args:
            message (str): Mensaje que dirá la persona
        """
        self.__speaking = True
        print(message)

    def run(self) -> None:
        """Cambia el estado de la persona a correr
        """
        self.__running = True

    def __format_age(self) -> str:
        """Da un formato a la edad, si es un decimal en rango [0.0, 0.12], serán meses, si es mayor a 

        Returns:
            str: _description_
        """
        if self.__age < 1 and len(str(self.__age).split('.')[1]) == 2 and self.__age > 0.12 or self.__age > 1 and type(self.__age % self.__age) == 'float':
            return 'Edad errónea'
        if self.__age >= 1:
              return f'{int(self.__age % 100)} {'año' if self.__age == 1 else 'años'}'
        else:
            age = int((self.__age * 10) % 10) if len(str(self.__age).split('.')[1]) == 1 else int((self.__age * 100) % 100)
            return f'{age} {'mes' if age < 2 else 'meses'}'