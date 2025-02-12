class Person:
    def __init__(self, name:str, age:float | int, weight:float | int, height:int):
        # Properties
        self.name:str = name # Nombre completo
        self.age:float = age # 0.0 hasta 0.12 Son meses, > son años
        self.weight:float = weight # Peso en Kg
        self.height:int = height # Altura en Centímetros
        # Actions
        self.walking:bool = False # ¿Está caminando?
        self.speaking:bool = False # ¿Está hablando?
        self.running:bool = False # ¿Está corriendo?
    
    def __str__(self) -> str:
        return f'Nombre: {self.name}\nEdad: {self.__format_age()}\nPeso: {self.weight} Kg\nAltura: {self.height} CM\n'

    def walk(self) -> None:
        """Cambia el estado de la persona a camninar
        """
        self.walking = True

    def speak(self, message:str) -> None:
        """Hace que la persona hable

        Args:
            message (str): Mensaje que dirá la persona
        """
        self.speaking = True
        print(message)

    def run(self) -> None:
        """Cambia el estado de la persona a correr
        """
        self.running = True

    def __format_age(self) -> str:
        """Da un formato a la edad, si es un decimal en rango [0.0, 0.12], serán meses, si es mayor a 

        Returns:
            str: _description_
        """
        if self.age < 1 and len(str(self.age).split('.')[1]) == 2 and self.age > 0.12 or self.age > 1 and type(self.age % self.age) == 'float':
            return 'Edad errónea'
        if self.age >= 1:
              # Formatear edad a años
              return f'{int(self.age % 100)} {'año' if self.age == 1 else 'años'}'
        else:
            # Formatear edad a meses
            age = int((self.age * 10) % 10) if len(str(self.age).split('.')[1]) == 1 else int((self.age * 100) % 100)
            return f'{age} {'mes' if age < 2 else 'meses'}'