def prov_vvod_time(time):
    if time[0].isdigit():
        if 0 <= int(time[0]) <= 23:
            prav_vvod_hour = True
        else:
            prav_vvod_hour = False
    else:
        prav_vvod_hour = False
        
    if time[1].isdigit():
        if 0 <= int(time[1]) <= 59:
            prav_vvod_minute = True
        else:
            prav_vvod_minute = False
    else:
        prav_vvod_minute = False
        
    if prav_vvod_hour and prav_vvod_minute:
        return True
    elif prav_vvod_hour and not prav_vvod_minute:
        print("Введены недопустимые данные: минуты должны быть от 0 до 59")
        return False
    elif not prav_vvod_hour and prav_vvod_minute:
        print("Введены недопустимые данные: часы должны быть от 0 до 23.")
        return False
    else:
        print("Введены недопустимые данные: часы должны быть от 0 до 23, минуты должны быть от 0 до 59.")
        return False
def prov_vvoda(vvod):
    time = list(vvod.split())
    if len(time) > 2:
        print("Введено больше двух чисел, надо ввести время в формате 'часы минуты'.")
        return False
    elif len(time) < 2:
        print("Введено меньше двух чисел, надо ввести время в формате 'часы минуты'.")
        return False
    else:
        return prov_vvod_time(time)
            
def main():
    print("Введите время в формате 'часы минуты':")
    vvod = input()
    if prov_vvoda(vvod):
        print("проверка пройдена")
if __name__ == "__main__":
    main()
