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

def pad_hour(hour):
    razg_hour = hour % 12
    if razg_hour == 0:
        return "12 часов"
    elif razg_hour == 1:
        return "1 час"
    elif 2 <= razg_hour <= 4:
        return "{} часа".format(razg_hour)
    else:
        return "{} часов".format(razg_hour)

def pad_minute(minute):
    if minute == 0:
        return "ровно"
    elif minute % 10 == 1 and minute != 11:
        return "{} минута".format(minute)
    elif 2 <= minute % 10 <= 4 and not(12 <= minute <= 14):
        return "{} минуты".format(minute)
    else:
        return "{} минут".format(minute)
    
def prom_time(hour):
    if 0 <= hour <= 5:
        return "ночи"
    elif 6 <= hour <= 11:
        return "утра"
    elif 12 <= hour <= 17:
        return "дня"
    else:
        return "вечера"

def main():
    print("Введите время в формате 'часы минуты':")
    vvod = input()
    while not prov_vvoda(vvod):
        print("Введите время в формате 'часы минуты':")
        vvod = input()
    if vvod == "00 00":
        print("полночь")
    elif vvod == "12 00":
        print("полдень")
    else:
        ch_time = list(map(int, vvod.split()))
        otv_time = pad_hour(ch_time[0])
        if ch_time[1] == 0:
            otv_time = "{} {} {}".format(pad_hour(ch_time[0]), prom_time(ch_time[0]), pad_minute(ch_time[1]))
        else:
            otv_time = "{} {} {}".format(pad_hour(ch_time[0]), pad_minute(ch_time[1]), prom_time(ch_time[0]))
        print(otv_time)
if __name__ == "__main__":
    main()
