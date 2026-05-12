import os
import csv
class Car:
    __ID = 0
    
    def __init__(self, brand, model, year, VIN, color, mileage, ID = 0):
        if not(isinstance(brand, str)) or (len(brand.strip()) == 0):
            raise ValueError("Марка машины должна быть непустой строкой")
        if not(isinstance(model, str)) or (len(model.strip()) == 0):
            raise ValueError("Модель машины должна быть непустой строкой")
        if not(isinstance(year, int)) or not(1886 <= year <= 2026):
            raise ValueError("Год выпуска машины должен быть целым числом от 1886 до 2026")
        if not(isinstance(VIN, str)) or (len(VIN) != 17):
            raise ValueError("VIN должен быть строкой длиной 17 из символов: 0123456789ABCDEFGHJKLMNPRSTUVWXYZ")  
        for sim in VIN:
            if not(sim in "0123456789ABCDEFGHJKLMNPRSTUVWXYZ"): 
                raise ValueError("VIN должен быть строкой длиной 17 из символов: 0123456789ABCDEFGHJKLMNPRSTUVWXYZ")
        if not(isinstance(color, str)) or (len(color.strip()) == 0):
            raise ValueError("Цвет машины должен быть непустой строкой")
        if not(isinstance(mileage, (int, float))) or (mileage < 0):
            raise ValueError("Пробег должен быть неотрицательным числом")     
        self._brand = brand
        self._model = model
        self._year = year
        self.__VIN = VIN
        self._color = color
        self._mileage = float(mileage)
        if ID == 0:
            Car.__ID += 1
            self.__car_ID = Car.__ID
            print(f"Создание ID {self.__car_ID}")
        else:
            self.__car_ID = ID    
            
    def __del__(self):
        print(f"Удаление ID {self.__car_ID}")
        
    def __str__(self):
        return (f"{self._brand} {self._model}: год выпуска = {self._year}; VIN = {self.__VIN}; цвет - {self._color}; пробег = {self._mileage} км; ID автомобиля = {self.__car_ID}")
    
    def __repr__(self):
        return (f"{self._brand}, {self._model}, {self._year}, {self.__VIN}, {self._color}, {self._mileage}, {self.__car_ID}")
    
    def __copy__(self):
        new_car = Car(self._brand, self._model, self._year, self.__VIN, self._color, self._mileage, self.__car_ID)
        return new_car
    
    def __eq__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return self._brand + self._model == other._brand + other._model
    
    def __ne__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return self._brand + self._model != other._brand + other._model
    
    def __lt__(self, other):
        if not isinstance(other, Car):
            return NotImplemented      
        return self._mileage < other._mileage
    
    def __le__(self, other):
        if not isinstance(other, Car):
            return NotImplemented      
        return self._mileage <= other._mileage   
    
    def __gt__(self, other):
        if not isinstance(other, Car):
            return NotImplemented      
        return self._mileage > other._mileage
    
    def __ge__(self, other):
        if not isinstance(other, Car):
            return NotImplemented      
        return self._mileage >= other._mileage
    
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, new_brand):
        if not(isinstance(new_brand, str)) or (len(new_brand.strip()) == 0):
            raise ValueError("Марка машины должна быть непустой строкой")
        self._brand = new_brand
        
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, new_model):
        if not(isinstance(new_model, str)) or (len(new_model.strip()) == 0):
            raise ValueError("Модель машины должна быть непустой строкой")
        self._model = new_model   
    
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, new_year):
        if not(isinstance(new_year, int)) or not(1886 <= new_year <= 2026):
            raise ValueError("Год выпуска машины должен быть целым числом от 1886 до 2026")
        self._year = new_year
    
    @property
    def VIN(self):
        return self.__VIN
    
    @VIN.setter
    def VIN(self, new_VIN):
        if not(isinstance(new_VIN, str)) or (len(new_VIN) != 17):
            raise ValueError("VIN должен быть строкой длиной 17 из символов: 0123456789ABCDEFGHJKLMNPRSTUVWXYZ")  
        for sim in new_VIN:
            if not(sim in "0123456789ABCDEFGHJKLMNPRSTUVWXYZ"): 
                raise ValueError("VIN должен быть строкой длиной 17 из символов: 0123456789ABCDEFGHJKLMNPRSTUVWXYZ")
        self.__VIN = new_VIN
        
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, new_color):
        if not(isinstance(new_color, str)) or (len(new_color.strip()) == 0):
            raise ValueError("Цвет машины должен быть непустой строкой")
        self._color = new_color
        
    @property
    def mileage(self):
        return self._mileage
    
    @mileage.setter
    def mileage(self, new_mileage):
        if not(isinstance(new_mileage, (int, float))) or (new_mileage < 0):
            raise ValueError("Пробег должен быть неотрицательным числом")
        self._mileage = float(new_mileage)
        
    @property
    def car_ID(self):
        return self.__car_ID
    
    @classmethod
    def from_string(cls, info):
        if not(isinstance(info, str)):
            raise ValueError('Введите через запятую марку автомобиля, модель автомобиля, год выпуска автомобиля, VIN автомобиля, цвет автомобиля и пробег автомобиля')
        info_lst = info.rstrip().split(", ")
        if not(5 < len(info_lst) < 8):
            raise ValueError('Введите через запятую марку автомобиля, модель автомобиля, год выпуска автомобиля, VIN автомобиля, цвет автомобиля и пробег автомобиля')
        try:
            info_lst[2] = int(info_lst[2])
        except:
            raise ValueError("Год выпуска машины должен быть целым числом от 1886 до 2026")
        try:
            info_lst[5] = float(info_lst[5])
        except:
            raise ValueError("Пробег должен быть неотрицательным числом")
        if len(info_lst) == 6:
            return cls(info_lst[0], info_lst[1], info_lst[2], info_lst[3], info_lst[4], info_lst[5])
        else:
            try:
                info_lst[6] = int(info_lst[6])
            except:
                raise ValueError("ID автомобиля должно быть положительным целым числом")           
            car = cls(info_lst[0], info_lst[1], info_lst[2], info_lst[3], info_lst[4], info_lst[5], info_lst[6])
            if car.car_ID > Car.__ID:
                Car.__ID = car.car_ID            
            return car
    
class Car_Database:
    def __init__(self, filename):
        if not(isinstance(filename, str)) or (len(filename.strip()) == 0):
            raise ValueError("Название файла должно быть непустой строкой")
        self.__filename = filename
        self._cars = list()
        if not(os.path.exists(filename)):
            with open(filename, "x", encoding = "utf-8") as database:
                pass
                
    @property
    def cars(self):
        return self._cars
    
    def read_database(self):
        self._cars = list()
        with open(self.__filename, "r", encoding = "utf-8") as database:
            for line in database.readlines():
                car = Car.from_string(line)
                self._cars.append(car)    
                
    def write_database(self):
        with open(self.__filename, "w", encoding = "utf-8") as database:
            for car in self._cars:
                print(repr(car), file = database)
    
    def sort_database_brand(self):
        for i in range(len(self._cars) - 1):
            for j in range(len(self._cars) - 1 - i):
                if self._cars[j].brand > self._cars[j + 1].brand:
                    self._cars[j], self._cars[j + 1] = self._cars[j + 1], self._cars[j]
    
    def sort_database_model(self):
        for i in range(len(self._cars) - 1):
            for j in range(len(self._cars) - 1 - i):
                if self._cars[j].model > self._cars[j + 1].model:
                    self._cars[j], self._cars[j + 1] = self._cars[j + 1], self._cars[j]
                    
    def sort_database_year(self):
        for i in range(len(self._cars) - 1):
            for j in range(len(self._cars) - 1 - i):
                if self._cars[j].year > self._cars[j + 1].year:
                    self._cars[j], self._cars[j + 1] = self._cars[j + 1], self._cars[j]
                    
    def sort_database_VIN(self):
        for i in range(len(self._cars) - 1):
            for j in range(len(self._cars) - 1 - i):
                if self._cars[j].VIN > self._cars[j + 1].VIN:
                    self._cars[j], self._cars[j + 1] = self._cars[j + 1], self._cars[j]
                    
    def sort_database_color(self):
        for i in range(len(self._cars) - 1):
            for j in range(len(self._cars) - 1 - i):
                if self._cars[j].color > self._cars[j + 1].color:
                    self._cars[j], self._cars[j + 1] = self._cars[j + 1], self._cars[j]    
    
    def sort_database_mileage(self):
        for i in range(len(self._cars) - 1):
            for j in range(len(self._cars) - 1 - i):
                if self._cars[j] > self._cars[j + 1]:
                    self._cars[j], self._cars[j + 1] = self._cars[j + 1], self._cars[j]
                    
    def sort_database_car_ID(self):
        for i in range(len(self._cars) - 1):
            for j in range(len(self._cars) - 1 - i):
                if self._cars[j].car_ID > self._cars[j + 1].car_ID:
                    self._cars[j], self._cars[j + 1] = self._cars[j + 1], self._cars[j]        
            
    def clear_database(self):
        self._cars = list()
        with open(self.__filename, "w", encoding = "utf-8") as database:
            pass
    
    def add_car(self, add_car):       
        if not(isinstance(add_car, Car)):
            raise ValueError("Добавить можно только автомобиль")
        for car in self._cars:
            if car.VIN == add_car.VIN:
                raise ValueError("Автомобиль уже был добавлен")
        self._cars.append(add_car)
        
    def delete_car(self, delete_car):
        if not(isinstance(delete_car, Car)):
            raise ValueError("Удалить можно только автомобиль")
        car_find = False
        for car in self._cars:
            if car.VIN == delete_car.VIN:
                car_find = True
                self._cars.remove(car)
        if not car_find:
            raise ValueError("Автомобиль не найден")
            
    def edit_car_brand(self, old_car, new_brand):
        if not(isinstance(old_car, Car)):
            raise ValueError("Редактировать можно только автомобиль")
        if not(old_car in self._cars):
            raise ValueError("Автомобиль не найден")
        if not(isinstance(new_brand, str)) or (len(new_brand.strip()) == 0):
            raise ValueError("Марка машины должна быть непустой строкой")        
        old_car.brand = new_brand
        
    def edit_car_model(self, old_car, new_model):
        if not(isinstance(old_car, Car)):
            raise ValueError("Редактировать можно только автомобиль")
        if not(old_car in self._cars):
            raise ValueError("Автомобиль не найден")
        if not(isinstance(new_model, str)) or (len(new_model.strip()) == 0):
            raise ValueError("Модель машины должна быть непустой строкой")        
        old_car.model = new_model   
        
    def edit_car_year(self, old_car, new_year):
        if not(isinstance(old_car, Car)):
            raise ValueError("Редактировать можно только автомобиль")
        if not(old_car in self._cars):
            raise ValueError("Автомобиль не найден")
        if not(isinstance(new_year, int)) or not(1886 <= new_year <= 2026):
            raise ValueError("Год выпуска машины должен быть целым числом от 1886 до 2026")        
        old_car.year = new_year
    
    def edit_car_VIN(self, old_car, new_VIN):
        if not(isinstance(old_car, Car)):
            raise ValueError("Редактировать можно только автомобиль")
        if not(old_car in self._cars):
            raise ValueError("Автомобиль не найден")
        if not(isinstance(new_VIN, str)) or (len(new_VIN) != 17):
            raise ValueError("VIN должен быть строкой длиной 17 из символов: 0123456789ABCDEFGHJKLMNPRSTUVWXYZ")  
        for sim in new_VIN:
            if not(sim in "0123456789ABCDEFGHJKLMNPRSTUVWXYZ"): 
                raise ValueError("VIN должен быть строкой длиной 17 из символов: 0123456789ABCDEFGHJKLMNPRSTUVWXYZ")
        for car in self._cars:
            if car.VIN == new_VIN and car != old_car:
                raise ValueError(f"VIN {new_VIN} уже принадлежит другому автомобилю")        
        old_car.VIN = new_VIN
        
    def edit_car_color(self, old_car, new_color):
        if not(isinstance(old_car, Car)):
            raise ValueError("Редактировать можно только автомобиль")
        if not(old_car in self._cars):
            raise ValueError("Автомобиль не найден")
        if not(isinstance(new_color, str)) or (len(new_color.strip()) == 0):
            raise ValueError("Цвет машины должен быть непустой строкой")        
        old_car.color = new_color
        
    def edit_car_mileage(self, old_car, new_mileage):
        if not(isinstance(old_car, Car)):
            raise ValueError("Редактировать можно только автомобиль")
        if not(old_car in self._cars):
            raise ValueError("Автомобиль не найден")
        if not(isinstance(new_mileage, (int, float))) or (new_mileage < 0):
            raise ValueError("Пробег должен быть неотрицательным числом")          
        old_car.mileage = new_mileage
    
    def view_cars(self):
        for car in self._cars:
            print(car)
            
    def find_car_by_brand(self, find_brand):
        if not(isinstance(find_brand, str)) or (len(find_brand.strip()) == 0):
            raise ValueError("Марка машины должна быть непустой строкой")
        results = list()
        for car in self._cars:
            if car.brand == find_brand:
                results.append(car)
        return results
    
    def find_car_by_model(self, find_model):
        if not(isinstance(find_model, str)) or (len(find_model.strip()) == 0):
            raise ValueError("Модель машины должна быть непустой строкой")
        results = list()
        for car in self._cars:
            if car.model == find_model:
                results.append(car)
        return results
    
    def find_car_by_year(self, year_from, year_to):
        if not(isinstance(year_from, int)) or not(1886 <= year_from <= 2026) or not(isinstance(year_to, int)) or not(1886 <= year_to <= 2026):
            raise ValueError("Год выпуска машины должен быть целым числом от 1886 до 2026")
        results = list()
        for car in self._cars:
            if min(year_to, year_from) <= car.year <= max(year_to, year_from):
                results.append(car)
        return results    
    
    def find_car_by_VIN(self, find_VIN):
        if not(isinstance(find_VIN, str)) or (len(find_VIN) != 17):
            raise ValueError("VIN должен быть строкой длиной 17 из символов: 0123456789ABCDEFGHJKLMNPRSTUVWXYZ")  
        for sim in find_VIN:
            if not(sim in "0123456789ABCDEFGHJKLMNPRSTUVWXYZ"): 
                raise ValueError("VIN должен быть строкой длиной 17 из символов: 0123456789ABCDEFGHJKLMNPRSTUVWXYZ")
        results = list()
        for car in self._cars:
            if car.VIN == find_VIN:
                results.append(car)
        return results   
    
    def find_car_by_color(self, find_color):
        if not(isinstance(find_color, str)) or (len(find_color.strip()) == 0):
            raise ValueError("Цвет машины должен быть непустой строкой")
        results = list()
        for car in self._cars:
            if car.color == find_color:
                results.append(car)
        return results
    
    def find_car_by_mileage(self, mileage_from, mileage_to):
        if not(isinstance(mileage_from, (int, float))) or (mileage_from < 0) or not(isinstance(mileage_to, (int, float))) or (mileage_to < 0):
            raise ValueError("Пробег должен быть неотрицательным числом") 
        results = list()
        for car in self._cars:
            if min(mileage_to, mileage_from) <= car.mileage <= max(mileage_to, mileage_from):
                results.append(car)
        return results
    
    def find_car_by_car_ID(self, find_ID):
        if not(isinstance(find_ID, int)) or (find_ID <= 0):
            raise ValueError("ID автомобиля должно быть положительным целым числом")
        results = list()
        for car in self._cars:
            if car.car_ID == find_ID:
                results.append(car)
        return results
    
    def export_csv(self):
        filename_lst = self.__filename.split(".")
        csv_name = filename_lst[0] + ".csv"
        with open(csv_name, "w", newline = "", encoding = "utf-8-sig") as csv_file:
            database_writer = csv.writer(csv_file, delimiter = ",")
            database_writer.writerow(['ID', 'Марка', 'Модель', 'Год выпуска', 'VIN', 'Цвет', 'Пробег (км)'])
            for car in self._cars:
                database_writer.writerow([car.car_ID, car.brand, car.model, car.year, car.VIN, car.color, car.mileage])
