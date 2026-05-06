class Planet:
    __ID = 0
    def __init__(self, name, radius, mass, distance_from_sun, planet_type):
        if not(isinstance(name, str)) or (len(name.strip()) == 0):
            raise ValueError("Название планеты должно быть непустой строкой")
        if not(isinstance(radius, (int, float))) or (radius <= 0):
            raise ValueError("Радиус должен быть положительным числом")
        if not(isinstance(mass, (int, float))) or (mass <= 0):
            raise ValueError("Масса должна быть положительным числом")
        if not(isinstance(distance_from_sun, (int, float))) or (distance_from_sun <= 0):
            raise ValueError("Расстояние от Солнца должно быть положительным числом")
        if not(isinstance(planet_type, str)) or ((planet_type != "каменная") and (planet_type != "газовый гигант") and (planet_type != "ледяной гигант")):
            raise ValueError("Типы планет: каменная, газовый гигант, ледяной гигант")
        Planet.__ID += 1
        self._name = name.strip()
        self._radius = float(radius)
        self._mass = float(mass)
        self._distance_from_sun = float(distance_from_sun)
        self._planet_type = planet_type
        self.__planet_ID = Planet.__ID
        print(f"Создание ID {self.__planet_ID}")
    
    def __del__(self):
        print(f"Удаление ID {self.__planet_ID}")
        Planet.__ID -= 1
        
    def __str__(self):
        return (f"Планета {self._name}: радиус = {self._radius} км; масса = {self._mass} кг; расстояние от Солнца = {self._distance_from_sun} млн км; тип планеты - {self._planet_type}; ID планеты = {self.__planet_ID}")
    
    def __repr__(self):
        return (f"{self._name}, {self._radius}, {self._mass}, {self._distance_from_sun}, {self._planet_type}, {self.__planet_ID}")
    
    def __copy__(self):
        new_planet = Planet(self._name, self._radius, self._mass, self._distance_from_sun, self._planet_type)
        return new_planet
    
    def __eq__(self, other):
        if not isinstance(other, Planet):
            return NotImplemented
        return self._name == other._name
    
    def __ne__(self, other):
        if not isinstance(other, Planet):
            return NotImplemented
        return self._name != other._name    
    
    def __lt__(self, other):
        if not isinstance(other, Planet):
            return NotImplemented      
        return self._distance_from_sun < other._distance_from_sun
    
    def __le__(self, other):
        if not isinstance(other, Planet):
            return NotImplemented      
        return self._distance_from_sun <= other._distance_from_sun   
    
    def __gt__(self, other):
        if not isinstance(other, Planet):
            return NotImplemented      
        return self._distance_from_sun > other._distance_from_sun
    
    def __ge__(self, other):
        if not isinstance(other, Planet):
            return NotImplemented      
        return self._distance_from_sun >= other._distance_from_sun      
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not(isinstance(new_name, str)) or (len(new_name.strip()) == 0):
            raise ValueError("Название планеты должно быть непустой строкой")
        self._name = new_name
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, new_radius):
        if not(isinstance(new_radius, (int, float))) or (new_radius <= 0):
            raise ValueError("Радиус должен быть положительным числом")
        self._radius = new_radius  
    
    @property
    def mass(self):
        return self._mass
    
    @mass.setter
    def mass(self, new_mass):
        if not(isinstance(new_mass, (int, float))) or (new_mass <= 0):
            raise ValueError("Масса должна быть положительным числом")
        self._mass = new_mass
        
    @property
    def distance_from_sun(self):
        return self._distance_from_sun
    
    @distance_from_sun.setter
    def distance_from_sun(self, new_distance_from_sun):
        if not(isinstance(new_distance_from_sun, (int, float))) or (new_distance_from_sun <= 0):
            raise ValueError("Расстояние от Солнца должно быть положительным числом")
        self._distance_from_sun = new_distance_from_sun
        
    @property
    def planet_type(self):
        return self._planet_type
    
    @planet_type.setter
    def planet_type(self, new_planet_type):
        if not(isinstance(new_planet_type, str)) or ((new_planet_type != "каменная") and (new_planet_type != "газовый гигант") and (new_planet_type != "ледяной гигант")):
            raise ValueError("Типы планет: каменная, газовый гигант, ледяной гигант")
        self._planet_type = new_planet_type
        
    @property
    def planet_ID(self):
        return self.__planet_ID
    
    @classmethod
    def planets_count(cls):
        return cls.__ID