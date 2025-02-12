def format_age(age) -> str:
        """Da un formato a la edad, si es un decimal en rango [0.0, 0.12], serán meses, si es mayor a 

        Args:
            age (float): Edad de la persona

        Returns:
            str: _description_
        """
        if age > 0.12 and age < 1 or age > 1 and type(age % age) == 'float':
            return 'Edad errónea'
        if age > 1:
              return f'{int(age % 100)} año/s'
        else:
            return f'{int((age * 10) % 10)} mese/s' if len(str(age).split('.')[1]) == 1 else f'{int((age * 100) % 100)} meses'

age = 0.12
# leng= len(str(age).split('.')[1])
print(format_age(age))