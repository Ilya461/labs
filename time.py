def prov_vvod_time(time):#Вторая проверка на правильный ввод часов
    #Ввод времени
    
    #Проверка на правильный ввод часов
    if time[0].isdigit():
        if 0 <= int(time[0]) <= 23:
            prav_vvod_hour = True
        else:
            prav_vvod_hour = False
    else:
        prav_vvod_hour = False

    #Проверка на правильный ввод минут
    if time[1].isdigit():
        if 0 <= int(time[1]) <= 59:
            prav_vvod_minute = True
        else:
            prav_vvod_minute = False
    else:
        prav_vvod_minute = False

    #Проверка пройдена, или указываем, из-за чего произошла ошибка
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

def prov_vvoda(vvod):#Первая проверка на правильный ввод часов
    #Вводим время
    time = list(vvod.split())#Разбиваем введённое время на часы и минуты
    #Проверяем, введены только часы и минуты, значит продолжаем проверку, или есть дополнительные элементы, тогда указываем ошибку
    if len(time) > 2:
        print("Введено больше двух чисел, надо ввести время в формате 'часы минуты'.")
        return False
    elif len(time) < 2:
        print("Введено меньше двух чисел, надо ввести время в формате 'часы минуты'.")
        return False
    else:
        return prov_vvod_time(time)

def obr_hour(hour):#Изменение формы слова "часы" и само значение часов
    #Вводим часы
    razg_hour = hour % 12
    #Изменяем форму слова "часы" в зависимости от количества часов
    if hour == 12:
        return "12 часов"
    elif hour == 0:
        return "0 часов"
    elif razg_hour == 1:
        return "1 час"
    elif 2 <= razg_hour <= 4:
        return "{} часа".format(razg_hour)
    else:
        return "{} часов".format(razg_hour)

def obr_minute(minute):#Изменение формы слова "минуты" и само значение минут
    #Вводим минуты
    #Изменяем форму слова "минуты" в зависимости от количества минут
    if minute == 0:
        return "ровно"
    elif minute % 10 == 1 and minute != 11:
        return "{} минута".format(minute)
    elif 2 <= minute % 10 <= 4 and not(12 <= minute <= 14):
        return "{} минуты".format(minute)
    else:
        return "{} минут".format(minute)
    
def prom_time(hour):#Обработка промежутка времени в зависимости от количества часов
    #Вводим часы
    #Выбираем правильный промежуток времени в зависимости от количества часов
    if 0 <= hour <= 5:
        return "ночи"
    elif 6 <= hour <= 11:
        return "утра"
    elif 12 <= hour <= 17:
        return "дня"
    else:
        return "вечера"

def main():#Начало
    print("Введите время в формате 'часы минуты':")
    vvod = input()#Вводим время
    while not prov_vvoda(vvod):#Проверка формата времени, если неправильный формат, то снова вводим время"
        print()
        print("Введите время в формате 'часы минуты':")
        vvod = input()
    #Обрабатываем случаи с полночью и полднем, и, если эти результаты не подходит, используем основной алгоритм
    if vvod == "00 00":
        print("полночь")
    elif vvod == "12 00":
        print("полдень")
    else:
        ch_time = list(map(int, vvod.split()))#Делим правильный формат времени на часы и минуты
        #Создаём строку с ответом. Если количество минут равно 0, то после обработки часов сначала добавляем промежуток времени, а потом слово "ровно"
        if ch_time[1] == 0:
            otv_time = "{} {} {}".format(obr_hour(ch_time[0]), prom_time(ch_time[0]), obr_minute(ch_time[1]))
        else:
            otv_time = "{} {} {}".format(obr_hour(ch_time[0]), obr_minute(ch_time[1]), prom_time(ch_time[0]))
        print(otv_time)#Выводим ответ
if __name__ == "__main__":
    main()
