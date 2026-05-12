import os
import csv
from car import Car, Car_Database
def choice_mode(min_value, max_value):
    while True:
        try:
            mode = int(input())
            if min_value <= mode <= max_value:
                return mode
            else:
                print(f"Введите число от {min_value} до {max_value}, обозначающее режим работы")
        except ValueError:
            print(f"Введите число от {min_value} до {max_value}, обозначающее режим работы")
            
def main():
    database = Car_Database("database_car.txt")
    database.read_database()
    print("База данных успешно загружена!")
    print()
    print("Выберите действие:")
    print("1 - Загрузка БД из файла")
    print("2 - Сохранение БД в файл")
    print("3 - Просмотр всех записей")
    print("4 - Добавление новой записи")
    print("5 - Поиск записи (по разным критериям)")
    print("6 - Редактирование записи")
    print("7 - Удаление записи")
    print("8 - Сортировка (по разным полям)")
    print("9 - Экспорт в CSV")    
    print("10 - Выход (Не забудьте сохранить в базу данных все изменения!)")
    mode = choice_mode(1, 10)
    while True:
        print()
        if mode == 1:
            database.read_database()
            print("База данных успешно загружена!")
            
        elif mode == 2:
            database.write_database()
            print("Все изменения успешно загружены в базу данных!")
            
        elif mode == 3:
            database.view_cars()
            
        elif mode == 4:
            print("Введите информацию о новом автомобиле по шаблону:")
            print("марка автомобиля, модель автомобиля, год выпуска автомобиля, VIN автомобиля, цвет автомобиля, пробег автомобиля")
            while True:
                str_car = input()
                try:
                    car = Car.from_string(str_car)
                    break
                except:
                    print("Введите информацию о новом автомобиле:")
            database.add_car(car)
            print("Автомобиль успешно добавлен в базу данных!")        
        
        elif mode == 5:
            print("Выберите поле, по которому будет происходить поиск записи:")
            print("1 - по марке автомобиля")
            print("2 - по модели")
            print("3 - по году выпуска")
            print("4 - по VIN")
            print("5 - по цвету")
            print("6 - по пробегу")
            print("7 - по ID")
            value_find = choice_mode(1, 7)
            if value_find == 1:
                print("Введите марку автомобиля для поиска:")
                while True:
                    find_brand = input()
                    if len(find_brand.strip()) != 0:
                        break
                    else:
                        print("Марка машины должна быть непустой строкой")
                results = database.find_car_by_brand(find_brand)
                
            elif value_find == 2:
                print("Введите модель автомобиля для поиска:")
                while True:
                    find_model = input()
                    if len(find_model.strip()) != 0:
                        break
                    else:
                        print("Модель машины должна быть непустой строкой")
                results = database.find_car_by_model(find_model)
            
            elif value_find == 3:
                print("Введите в одной строке через пробел два года выпуска автомобиля для поиска(промежуток, среди которого ищутся записи):")
                while True:
                    find_years = input().split()
                    if len(find_years) == 2:
                        try:
                            if (1886 <= int(find_years[0]) <= 2026) and (1886 <= int(find_years[1]) <= 2026):
                                break
                        except:
                            print("Год выпуска машины должен быть целым числом от 1886 до 2026")
                    else:
                        print("Введите в одной строке через пробел два года выпуска автомобиля для поиска(промежуток, среди которого ищутся записи):")
                results = database.find_car_by_year(int(find_years[0]), int(find_years[1]))
                
            elif value_find == 4:
                print("Введите VIN автомобиля для поиска:")
                while True:
                    find_VIN = input()
                    if len(find_VIN) == 17:
                        correct_VIN = True
                        for sim in find_VIN:
                            if not(sim in "0123456789ABCDEFGHJKLMNPRSTUVWXYZ"): 
                                correct_VIN = False
                        if correct_VIN:
                            break
                        else:
                            print("VIN должен быть строкой длиной 17 из символов: 0123456789ABCDEFGHJKLMNPRSTUVWXYZ")
                    else:
                        print("VIN должен быть строкой длиной 17 из символов: 0123456789ABCDEFGHJKLMNPRSTUVWXYZ")
                results = database.find_car_by_VIN(find_VIN)
                
            elif value_find == 5:
                print("Введите цвет автомобиля для поиска:")
                while True:
                    find_color = input()
                    if len(find_color.strip()) != 0:
                        break
                    else:
                        print("Цвет машины должен быть непустой строкой")
                results = database.find_car_by_color(find_color)
                
            elif value_find == 6:
                print("Введите в одной строке через пробел два пробега автомобиля для поиска(промежуток, среди которого ищутся записи):")
                while True:
                    find_mileages = input().split()
                    if len(find_mileages) == 2:
                        try:
                            if (0 <= float(find_mileages[0])) and (0 <= float(find_mileages[1])):
                                break
                        except:
                            print("Пробег должен быть неотрицательным числом")
                    else:
                        print("Введите в одной строке через пробел два пробега автомобиля для поиска(промежуток, среди которого ищутся записи):")
                results = database.find_car_by_mileage(float(find_mileages[0]), float(find_mileages[1]))
                        
            elif value_find == 7:
                print("Введите ID автомобиля для поиска:")
                while True:
                    find_car_ID = input()
                    try:
                        if int(find_car_ID) > 0:
                            break
                        else:
                            print("ID машины должен быть положительным целым числом")
                    except:
                        print("ID машины должен быть положительным целым числом")
                results = database.find_car_by_car_ID(int(find_car_ID))
                
            if len(results) == 0:
                print("Таких автомобилей нет")
            else:
                for car in results:
                    print(car)
                    
        elif mode == 6:
            print("Выберите автомобиль по:")
            print("1 - по VIN")
            print("2 - по ID")
            value_choice = choice_mode(1, 2)
            if value_choice == 1:
                print("Введите VIN автомобиля для редактирования:")
                while True:
                    find_VIN = input()
                    if len(find_VIN) == 17:
                        correct_VIN = True
                        for sim in find_VIN:
                            if not(sim in "0123456789ABCDEFGHJKLMNPRSTUVWXYZ"): 
                                correct_VIN = False
                        if correct_VIN:
                            break
                        else:
                            print("VIN должен быть строкой длиной 17 из символов: 0123456789ABCDEFGHJKLMNPRSTUVWXYZ")
                    else:
                        print("VIN должен быть строкой длиной 17 из символов: 0123456789ABCDEFGHJKLMNPRSTUVWXYZ")
                results = database.find_car_by_VIN(find_VIN)
            
            else:
                print("Введите ID автомобиля для редактирования:")
                while True:
                    find_car_ID = input()
                    try:
                        if int(find_car_ID) > 0:
                            break
                        else:
                            print("ID машины должен быть положительным целым числом")
                    except:
                        print("ID машины должен быть положительным целым числом")
                results = database.find_car_by_car_ID(int(find_car_ID))
            
            if len(results) > 0:
                car_edit = results[0]
                print("Выберите поле, которое нужно отредактировать:")
                print("1 - марка автомобиля")
                print("2 - модель")
                print("3 - год выпуска")
                print("4 - VIN")
                print("5 - цвет")
                print("6 - пробег")
                value_edit = choice_mode(1, 6)
                if value_edit == 1:
                    print("Введите новую марку автомобиля:")
                    while True:
                        new_brand = input()
                        if len(new_brand.strip()) != 0:
                            break
                        else:
                            print("Марка машины должна быть непустой строкой")
                    database.edit_car_brand(car_edit, new_brand)
                
                elif value_edit == 2:
                    print("Введите новую модель автомобиля:")
                    while True:
                        new_model = input()
                        if len(new_model.strip()) != 0:
                            break
                        else:
                            print("Модель машины должна быть непустой строкой")
                    database.edit_car_model(car_edit, new_model)
                
                elif value_edit == 3:
                    print("Введите новый год выпуска автомобиля:")
                    while True:
                        new_year = input()
                        try:
                            if 1886 <= int(new_year) <= 2026:
                                break
                            else:
                                print("Год выпуска машины должен быть целым числом от 1886 до 2026")
                        except:
                            print("Год выпуска машины должен быть целым числом от 1886 до 2026")
                    database.edit_car_year(car_edit, int(new_year))                
                
                elif value_edit == 4:
                    print("Введите новый VIN автомобиля:")
                    while True:
                        new_VIN = input()
                        if len(new_VIN) == 17:
                            correct_VIN = True
                            for sim in new_VIN:
                                if not(sim in "0123456789ABCDEFGHJKLMNPRSTUVWXYZ"): 
                                    correct_VIN = False
                            if correct_VIN:
                                break
                            else:
                                print("VIN должен быть строкой длиной 17 из символов: 0123456789ABCDEFGHJKLMNPRSTUVWXYZ")
                        else:
                            print("VIN должен быть строкой длиной 17 из символов: 0123456789ABCDEFGHJKLMNPRSTUVWXYZ")
                    database.edit_car_VIN(car_edit, new_VIN)
                    
                elif value_edit == 5:
                    print("Введите новый цвет автомобиля:")
                    while True:
                        new_color = input()
                        if len(new_color.strip()) != 0:
                            break
                        else:
                            print("Цвет машины должен быть непустой строкой")
                    database.edit_car_color(car_edit, new_color)
                    
                elif value_edit == 6:
                    print("Введите новый пробег автомобиля:")
                    while True:
                        new_mileage = input()
                        try:
                            if float(new_mileage) >= 0:
                                break
                            else:
                                print("Пробег должен быть неотрицательным числом")
                        except:
                            print("Пробег должен быть неотрицательным числом")
                    database.edit_car_mileage(car_edit, float(new_mileage))
                                         
                print("Поле успешно изменено!")
            else:
                print("Автомобиль не найден")        
        
        elif mode == 7:
            print("Выберите по какому полю удалить автомобиль:")
            print("1 - по VIN")
            print("2 - по ID")
            value_delete = choice_mode(1, 2)
            if value_delete == 1:
                print("Введите VIN автомобиля для удаления:")
                while True:
                    delete_VIN = input()
                    if len(delete_VIN) == 17:
                        correct_VIN = True
                        for sim in delete_VIN:
                            if not(sim in "0123456789ABCDEFGHJKLMNPRSTUVWXYZ"): 
                                correct_VIN = False
                        if correct_VIN:
                            break
                        else:
                            print("VIN должен быть строкой длиной 17 из символов: 0123456789ABCDEFGHJKLMNPRSTUVWXYZ")
                    else:
                        print("VIN должен быть строкой длиной 17 из символов: 0123456789ABCDEFGHJKLMNPRSTUVWXYZ")
                results = database.find_car_by_VIN(delete_VIN)
            
            else:
                print("Введите ID автомобиля для удаления:")
                while True:
                    delete_car_ID = input()
                    try:
                        if int(delete_car_ID) > 0:
                            break
                        else:
                            print("ID машины должен быть положительным целым числом")
                    except:
                        print("ID машины должен быть положительным целым числом")
                results = database.find_car_by_car_ID(int(delete_car_ID))
            if len(results) > 0:
                database.delete_car(results[0])
                print("Автомобиль успешно удалён!")
            else:
                print("Автомобиль не найден")        
        
        elif mode == 8:
            print("Выберите поле, по которому будет происходить сортировка:")
            print("1 - по марке автомобиля")
            print("2 - по модели")
            print("3 - по году выпуска")
            print("4 - по VIN")
            print("5 - по цвету")
            print("6 - по пробегу")
            print("7 - по ID")
            value_sort = choice_mode(1, 7)
            if value_sort == 1:
                database.sort_database_brand()
            elif value_sort == 2:
                database.sort_database_model()
            elif value_sort == 3:
                database.sort_database_year()
            elif value_sort == 4:
                database.sort_database_VIN()
            elif value_sort == 5:
                database.sort_database_color()
            elif value_sort == 6:
                database.sort_database_mileage() 
            elif value_sort == 7:
                database.sort_database_car_ID()
            print("База данных успешно отсортирована!")
            
        elif mode == 9:
            database.export_csv()
            filename_lst = database.filename.split(".")
            csv_name = filename_lst[0] + ".csv"            
            print(f"Файл {csv_name} успешно создан!")
            
        elif mode == 10:
            print("Вы уверены, что сохранили все изменения или не хотите их сохранять?")
            print("1 - да")
            print("2 - нет")
            while True:
                ans = input()
                try:
                    if int(ans) in (1, 2):
                        break
                    else:
                        print("Введите цифру, означающую ваш ответ")
                except:
                    print("Введите цифру, означающую ваш ответ") 
            if int(ans) == 1:
                break
                           
        print()
        print("Выберите действие:")
        print("1 - Загрузка БД из файла")
        print("2 - Сохранение БД в файл")
        print("3 - Просмотр всех записей")
        print("4 - Добавление новой записи")
        print("5 - Поиск записи (по разным критериям)")
        print("6 - Редактирование записи")
        print("7 - Удаление записи")
        print("8 - Сортировка (по разным полям)")
        print("9 - Экспорт в CSV")    
        print("10 - Выход (Не забудьте сохранить в базу данных все изменения!)")
        mode = choice_mode(1, 10)

if __name__ == "__main__":
    main()