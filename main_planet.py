import os
from planet import Planet, Planet_Database
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
    database = Planet_Database("database_planet.txt")
    database.read_database()
    print("База данных успешно загружена!")
    print()
    print("Выберите действие:")
    print("1 - Чтение из БД")
    print("2 - Запись в БД")
    print("3 - Сортировка БД по выбранному полю")
    print("4 - Добавление нового объекта в БД")
    print("5 - Удаление объекта из БД")
    print("6 - Редактирование объекта в БД")
    print("7 - Вывод БД на экран")
    print("8 - Выход(Не забудьте сохранить в базу данных все изменения!)")
    mode = choice_mode(1, 8)
    while True:
        print()
        if mode == 1:
            database.read_database()
            print("База данных успешно загружена!")
            
        elif mode == 2:
            database.write_database()
            print("Все изменения успешно загружены в базу данных!")
            
        elif mode == 3:
            print("Выберите поле, по которому будет происходить сортировка:")
            print("1 - по имени планеты")
            print("2 - по радиусу")
            print("3 - по массе")
            print("4 - по расстоянию от Солнца до планеты")
            print("5 - по типу планеты")
            print("6 - по ID")
            value = choice_mode(1, 6)
            if value == 1:
                database.sort_database_name()
            elif value == 2:
                database.sort_database_radius()
            elif value == 3:
                database.sort_database_mass()
            elif value == 4:
                database.sort_database_distance_from_sun()
            elif value == 5:
                database.sort_database_planet_type()
            else:
                database.sort_database_planet_ID()            
            print("База данных успешно отсортирована!")
            
        elif mode == 4:
            print("Введите информацию о новой планете по шаблону:")
            print("имя планеты, радиус планеты, масса планеты, расстояние от Солнца до планеты, тип планеты")
            print("*типы планет: каменная, газовый гигант, ледяной гигант")
            while True:
                str_planet = input()
                try:
                    pl = Planet.from_string(str_planet)
                    break
                except:
                    print("Введите информацию о новой планете:")
            database.add_planet(pl)
            print("Планета успешно добавлена в базу данных!")
        
        elif mode == 5:
            print("Выберите по какому полю удалить планету:")
            print("1 - по имени планеты")
            print("2 - по ID")
            value_delete = choice_mode(1, 2)
            flag = False
            if value_delete == 1:
                print("Введите имя планеты:")
                while True:
                        name_planet = input()
                        if len(name_planet.strip()) != 0:
                            break
                        else:
                            print("Название планеты должно быть непустой строкой")
                for planet in database.planets:
                    if planet.name == name_planet:
                        database.delete_planet(planet)
                        flag = True
            else:
                print("Введите ID планеты:")
                while True:
                    ID_planet = input()
                    try:
                        ID = int(ID_planet)
                        if ID > 0:
                            break
                    except:
                        print("ID планеты - это целое положительное число")
                    print("ID планеты - это целое положительное число")
                for planet in database.planets:
                    if planet.planet_ID == ID:
                        database.delete_planet(planet)
                        flag = True
            if flag:
                print("Планета успешно удалена!")
            else:
                print("Планета не найдена")
        
        elif mode == 6:
            print("Выберите планету по:")
            print("1 - по имени")
            print("2 - по ID")
            value_choice = choice_mode(1, 2)
            flag = False
            if value_choice == 1:
                print("Введите имя планеты:")
                while True:
                        name_planet = input()
                        if len(name_planet.strip()) != 0:
                            break
                        else:
                            print("Название планеты должно быть непустой строкой")
                for planet in database.planets:
                    if planet.name == name_planet:
                        flag = True
                        break
            else:
                print("Введите ID планеты:")
                while True:
                    ID_planet = input()
                    try:
                        ID = int(ID_planet)
                        if ID > 0:
                            break
                    except:
                        print("ID планеты - это целое положительное число")
                    print("ID планеты - это целое положительное число")
                for planet in database.planets:
                    if planet.planet_ID == ID:
                        flag = True
                        break
            if flag:
                print("Выберите поле, которое нужно отредактировать:")
                print("1 - имя планеты")
                print("2 - радиус")
                print("3 - массу")
                print("4 - расстояние от Солнца до планеты")
                print("5 - тип планеты")
                value_edit = choice_mode(1, 5)
                if value_edit == 1:
                    print("Введите новое имя планеты:")
                    while True:
                        new_name_planet = input()
                        if len(new_name_planet.strip()) != 0:
                            break
                        else:
                            print("Название планеты должно быть непустой строкой")
                    database.edit_planet_name(planet, new_name_planet)
                
                elif value_edit == 2:
                    print("Введите новый радиус планеты:")
                    while True:
                        new_radius_planet = input()
                        try:
                            new_radius = float(new_radius_planet)
                            if new_radius > 0:
                                break
                        except:
                            print("Радиус планеты - это положительное число")
                        print("Радиус планеты - это положительное число")
                    database.edit_planet_radius(planet, new_radius)
                
                elif value_edit == 3:
                    print("Введите новую массу планеты:")
                    while True:
                        new_mass_planet = input()
                        try:
                            new_mass = float(new_mass_planet)
                            if new_mass > 0:
                                break
                        except:
                            print("Масса планеты - это положительное число")
                        print("Масса планеты - это положительное число")
                    database.edit_planet_mass(planet, new_mass)
                
                elif value_edit == 4:
                    print("Введите новое расстояние от Солнца до планеты:")
                    while True:
                        new_distance_from_sun_to_planet = input()
                        try:
                            new_distance_from_sun = float(new_distance_from_sun_to_planet)
                            if new_distance_from_sun > 0:
                                break
                        except:
                            print("Расстояние от Солнца до планеты - это положительное число")
                        print("Расстояние от Солнца до планеты - это положительное число")
                    database.edit_planet_distance_from_sun(planet, new_distance_from_sun)
                
                else:
                    print("Введите новый тип планеты:")
                    while True:
                        new_planet_type = input()
                        if new_planet_type in ("каменная", "газовый гигант", "ледяной гигант"):
                            break
                        else:
                            print("Типы планет: каменная, газовый гигант, ледяной гигант")
                    database.edit_planet_planet_type(planet, new_planet_type)
                                         
                print("Поле успешно изменено!")
            else:
                print("Планета не найдена")
        
        elif mode == 7:
            database.view_planets()
            
        elif mode == 8:
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
        print("1 - Чтение из БД")
        print("2 - Запись в БД")
        print("3 - Сортировка БД по выбранному полю")
        print("4 - Добавление нового объекта в БД")
        print("5 - Удаление объекта из БД")
        print("6 - Редактирование объекта в БД")
        print("7 - Вывод БД на экран")
        print("8 - Выход(Не забудьте сохранить в базу данных все изменения!)")
        mode = choice_mode(1, 8)
    
if __name__ == "__main__":
    main()
