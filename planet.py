import os
class Planet:
    __ID = 0
    def __init__(self, name, radius, mass, distance_from_sun, planet_type, ID = 0):
        if not(isinstance(name, str)) or (len(name.strip()) == 0):
            raise ValueError("Название планеты должно быть непустой строкой")
        if not(isinstance(radius, (int, float))) or (radius <= 0):
            raise ValueError("Радиус должен быть положительным числом")
        if not(isinstance(mass, (int, float))) or (mass <= 0):
            raise ValueError("Масса должна быть положительным числом")
        if not(isinstance(distance_from_sun, (int, float))) or (distance_from_sun <= 0):
            raise ValueError("Расстояние от Солнца должно быть положительным числом")
        if not(isinstance(planet_type, str)) or not(planet_type in ("каменная", "газовый гигант", "ледяной гигант")):
            raise ValueError("Типы планет: каменная, газовый гигант, ледяной гигант")
        self._name = name.strip()
        self._radius = float(radius)
        self._mass = float(mass)
        self._distance_from_sun = float(distance_from_sun)
        self._planet_type = planet_type
        Planet.__ID += 1
        if ID == 0:
            self.__planet_ID = Planet.__ID
            print(f"Создание ID {self.__planet_ID}")
        else:
            self.__planet_ID = ID
    
    def __del__(self):
        print(f"Удаление ID {self.__planet_ID}")
        
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
        self._radius = float(new_radius)  
    
    @property
    def mass(self):
        return self._mass
    
    @mass.setter
    def mass(self, new_mass):
        if not(isinstance(new_mass, (int, float))) or (new_mass <= 0):
            raise ValueError("Масса должна быть положительным числом")
        self._mass = float(new_mass)
        
    @property
    def distance_from_sun(self):
        return self._distance_from_sun
    
    @distance_from_sun.setter
    def distance_from_sun(self, new_distance_from_sun):
        if not(isinstance(new_distance_from_sun, (int, float))) or (new_distance_from_sun <= 0):
            raise ValueError("Расстояние от Солнца должно быть положительным числом")
        self._distance_from_sun = float(new_distance_from_sun)
        
    @property
    def planet_type(self):
        return self._planet_type
    
    @planet_type.setter
    def planet_type(self, new_planet_type):
        if not(isinstance(new_planet_type, str)) or not(new_planet_type in ("каменная", "газовый гигант", "ледяной гигант")):
            raise ValueError("Типы планет: каменная, газовый гигант, ледяной гигант")
        self._planet_type = new_planet_type
        
    @property
    def planet_ID(self):
        return self.__planet_ID
    
    @planet_ID.setter
    def planet_ID(self, new_planet_ID):
        if not(isinstance(new_planet_ID, int)) or (new_planet_ID <= 0):
            raise ValueError("ID планеты должно быть положительным целым числом")
        self.__planet_ID = new_planet_ID
    
    @classmethod
    def planets_max_ID(cls):
        return cls.__ID
    
    @classmethod
    def add_ID(cls, add_ID):
        if not(isinstance(add_ID, int)) or (add_ID <= 0):
            raise ValueError("Добавить к ID можно только положительное целое число")
        cls.__ID += add_ID
    
    @classmethod
    def from_string(cls, info):
        if not(isinstance(info, str)):
            raise ValueError('Введите через запятую имя планеты, радиус планеты, массу планеты, расстояние от солнца до планеты и тип планеты')
        info_lst = info.rstrip().split(", ")
        if not(4 < len(info_lst) < 7):
            raise ValueError('Введите через запятую имя планеты, радиус планеты, массу планеты, расстояние от солнца до планеты и тип планеты')
        try:
            info_lst[1] = float(info_lst[1])
        except ValueError:
            raise ValueError("Радиус должен быть положительным числом")
        try:
            info_lst[2] = float(info_lst[2])
        except ValueError:
            raise ValueError("Масса должна быть положительным числом")
        try:
            info_lst[3] = float(info_lst[3])
        except ValueError:
            raise ValueError("Расстояние от Солнца должно быть положительным числом")
        if len(info_lst) == 5:
            return cls(info_lst[0], info_lst[1], info_lst[2], info_lst[3], info_lst[4])
        elif len(info_lst) == 6:
            try:
                info_lst[5] = int(info_lst[5])
            except ValueError:
                raise ValueError("ID планеты должно быть положительным целым числом")
            return cls(info_lst[0], info_lst[1], info_lst[2], info_lst[3], info_lst[4], info_lst[5])


class Planet_Database:
    def __init__(self, filename):
        if not(isinstance(filename, str)) or (len(filename.strip()) == 0):
            raise ValueError("Название файла должно быть непустой строкой")
        self.__filename = filename
        self._planets = list()
        if not(os.path.exists(filename)):
            with open(filename, "x", encoding = "utf-8") as database:
                pass
                
    @property
    def planets(self):
        return self._planets
    
    def read_database(self):
        self._planets = list()
        with open(self.__filename, "r", encoding = "utf-8") as database:
            for line in database.readlines():
                planet = Planet.from_string(line)
                self._planets.append(planet)    
                
    def write_database(self):
        with open(self.__filename, "w", encoding = "utf-8") as database:
            for planet in self._planets:
                print(repr(planet), file = database)
        
    def sort_database(self, mode):
        if not(mode in (1, 2, 3, 4, 5, 6)):
            raise ValueError("Введите 1, чтобы сортировать по имени планеты; 2 - по радиусу; 3 - по массе; 4 - по расстоянию от Солнца до планеты; 5 - по типу планеты; 6 - по ID")
        
        if mode == 1:
            for i in range(len(self._planets) - 1):
                for j in range(len(self._planets) - 1 - i):
                    if self._planets[j].name > self._planets[j + 1].name:
                        self._planets[j], self._planets[j + 1] = self._planets[j + 1], self._planets[j] 
        
        elif mode == 2:
            for i in range(len(self._planets) - 1):
                for j in range(len(self._planets) - 1 - i):
                    if self._planets[j].radius > self._planets[j + 1].radius:
                        self._planets[j], self._planets[j + 1] = self._planets[j + 1], self._planets[j] 
        
        elif mode == 3:
            for i in range(len(self._planets) - 1):
                for j in range(len(self._planets) - 1 - i):
                    if self._planets[j].mass > self._planets[j + 1].mass:
                        self._planets[j], self._planets[j + 1] = self._planets[j + 1], self._planets[j] 
                        
        elif mode == 4:
            for i in range(len(self._planets) - 1):
                for j in range(len(self._planets) - 1 - i):
                    if self._planets[j] > self._planets[j + 1]:
                        self._planets[j], self._planets[j + 1] = self._planets[j + 1], self._planets[j]
        
        elif mode == 5:
            for i in range(len(self._planets) - 1):
                for j in range(len(self._planets) - 1 - i):
                    if self._planets[j].planet_type > self._planets[j + 1].planet_type:
                        self._planets[j], self._planets[j + 1] = self._planets[j + 1], self._planets[j] 
                    
        else:
            for i in range(len(self._planets) - 1):
                for j in range(len(self._planets) - 1 - i):
                    if self._planets[j].planet_ID > self._planets[j + 1].planet_ID:
                        self._planets[j], self._planets[j + 1] = self._planets[j + 1], self._planets[j]         
    
    def clear_database(self):
        self._planets = list()
        with open(self.__filename, "w", encoding = "utf-8") as database:
            pass
    
    def add_planet(self, planet):       
        if not(isinstance(planet, Planet)):
            raise ValueError("Добавить можно только планету")
        if planet in self._planets:
            raise ValueError("Планета уже была добавлена")
        self._planets.append(planet)
        
    def delete_planet(self, planet):
        if not(isinstance(planet, Planet)):
            raise ValueError("Удалить можно только планету")
        if not(planet in self._planets):
            raise ValueError("Планета не найдена")
        self._planets.remove(planet)
         
    def edit_planet(self, old_planet, new_name = None, new_radius = None, new_mass = None, new_distance_from_sun = None, new_planet_type = None):
        if not(isinstance(old_planet, Planet)):
            raise ValueError("Редактировать можно только планету")
        if not(old_planet in self._planets):
            raise ValueError("Планета не найдена")
        if not(new_name is None):
            for planet in self._planets:
                if (planet.name == new_name) and (planet != old_planet):
                    raise ValueError("Планета с таким названием уже есть")
            old_planet.name = new_name
        if not(new_radius is None):
            old_planet.radius = new_radius
        if not(new_mass is None):
            old_planet.mass = new_mass
        if not(new_distance_from_sun is None):
            old_planet.distance_from_sun = new_distance_from_sun
        if not(new_planet_type is None):
            old_planet.planet_type = new_planet_type
    
    def view_planets(self):
        for planet in self._planets:
            print(planet)
