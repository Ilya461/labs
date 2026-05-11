class Car:
    __ID = 0
    
    def __init__(self, brand, model, year, VIN, color, mileage, ID = 0, creation_inf = True):
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
            if creation_inf:
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
        new_car = Car(self._brand, self._model, self._year, self.__VIN, self._color, self._mileage, self.__car_ID, False)
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