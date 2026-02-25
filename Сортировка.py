import random
def pr(s):
    s_pr = s.replace("-", "")
    lst = s_pr.split()
    if len(lst) == 0:
        return False
    else:
        flag = True
        for i in lst:
            if not i.isdigit():
                flag = False
        return flag
    
def pr_ind(ind, end):
    flag = False
    if ind.isdigit():
        if 0 <= int(ind) <= end:
            flag = True
    return flag

def selection_sort(lst):
    col_sr = col_perest = 0
    for i in range(len(lst) - 1):
        mn_ind, col_sr = (find_min_ind(lst, i))[0], col_sr + (find_min_ind(lst, i))[1]
        lst[i], lst[mn_ind] = lst[mn_ind], lst[i]
        col_perest += 1
    return ["выбором", col_sr, col_perest, lst]

def find_min_ind(lst, start):
    work_lst = (lst[start:]).copy()
    col_sr = 0
    min_ind = 0
    for i in range(1, len(work_lst)):
        col_sr += 1
        if work_lst[min_ind] > work_lst[i]:
            min_ind = i
    return [min_ind + start, col_sr]

def bubble_sort(lst):
    col_sr = col_perest = perest = 0
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            col_sr += 1
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                perest += 1
        if perest == 0:
            break
        col_perest, perest = col_perest + perest, 0
    return ["пузырьком", col_sr, col_perest, lst]

def merge_sort(lst):
    if len(lst) == 1:
        return [0, 0, lst]
    else:
        lch = lst[:(len(lst) // 2)]
        rch = lst[(len(lst) // 2):]
        col_sr_l, col_perest_l, lch = merge_sort(lch)
        col_sr_r, col_perest_r, rch = merge_sort(rch)
        col_sr_m, col_perest_m, merge_lst = merge(lch, rch)
        return [(col_sr_m + col_sr_l + col_sr_r), (col_perest_m + col_perest_l + col_perest_r), merge_lst]
    
def merge(lch, rch):
    lst = []
    l = r = col_sr = col_perest = 0
    while (len(lch) > l) and (len(rch) > r):
        if lch[l] < rch[r]:
            lst.append(lch[l])
            l += 1
        else:
            lst.append(rch[r])
            r += 1
        col_sr += 1
        col_perest += 1
    while l < len(lch):
        lst.append(lch[l])
        l += 1
        col_perest += 1
    while r < len(rch):
        lst.append(rch[r])
        r += 1
        col_perest += 1
    return col_sr, col_perest, lst

def vivod(lst):
    lst_s, lst_b, lst_m = lst.copy(), lst.copy(), lst.copy()
    srt_s, srt_b, srt_m = selection_sort(lst_s), bubble_sort(lst_b), merge_sort(lst_m)
    srt_m.insert(0, "слиянием")
    print("Сортировка выбором:", *(srt_s[3]))
    print("Сортировка пузырьком:", *(srt_b[3]))
    print("Сортировка слиянием:", *(srt_m[3]))
    lst_form = ["Сортировка", "Количество сравнений", "Количество перестановок"]
    otv = [lst_form, srt_s, srt_b, srt_m]
    print()
    for i in range(4):
        for j in range(3):
            print(str(otv[i][j]).ljust(27), end = "")
        print()
        
        
def main():
    print("Выберите режим работы:")
    print("1 - демонстративный")
    print("2 - интерактивный")
    flag = False
    while not flag:
        mode = input()
        if (mode != "1") and (mode != "2"):
            print("Введите цифру: 1 или 2, обозначающую режим работы:")
        else:
            flag = True
    if mode == "1":
        lst = [random.randint(0, 99) for _ in range(10)]
        print("Массив для сортировки:")
        print(*lst)
        vivod(lst)
    elif mode == "2":
        lst = []
        deistv = 0
        while deistv != "8":
            print()
            print("Выберите действие:")
            print("1 - ввести массив или ввести заново")
            print("2 - вывести массив")
            print("3 - изменить массив")
            print("4 - сортировка выбором")
            print("5 - сортировка пузырьком")
            print("6 - сортировка слиянием")
            print("7 - вывод таблицы сравнения сортировок")
            print("8 - выход")
            deistv = input()
            
            while (deistv != "1") and (deistv != "2") and (deistv != "3") and (deistv != "4") and (deistv != "5") and (deistv != "6") and (deistv != "7") and (deistv != "8"):
                print("Введите цифру: 1, 2, 3, 4, 5, 6, 7 или 8, обозначающую действие:")
                deistv = input()
            
            if deistv == "1":
                print("Введите целые числа для массива на одной строке, через пробел:")
                lst = input()
                while (not pr(lst)) or len(lst) == 0:
                    print("Введите целые числа для массива на одной строке, через пробел:")
                    lst = input()
                lst = list(map(int, lst.split()))
                print("Вы успешно ввели массив!")
            
            elif deistv == "2":
                if len(lst) == 0:
                    print("Вы ещё не ввели массив!")
                else:                  
                    print("Текущий массив:")
                    print(*lst)
                    
            elif deistv == "3":
                if len(lst) == 0:
                    print("Вы ещё не ввели массив!")
                else:            
                    print("Выберите действие:")
                    print("1 - изменить элемент массива")
                    print("2 - изменить часть массива")
                    deistv_izm = input()
                    while (deistv_izm != "1") and (deistv_izm != "2"):
                        print("Введите цифру: 1 или 2, обозначающую действие:")
                        deistv_izm = input()
                    
                    if deistv_izm == "1":
                        print("Введите номер элемента, начиная с 0 и заканчивая ", (len(lst) - 1), ":", sep = "")
                        ind = input()
                        end = len(lst) - 1
                        while not pr_ind(ind, end):
                            print("Введите номер элемента, начиная с 0 и заканчивая ", (len(lst) - 1), ":", sep = "")
                            ind = input()
                        print("Введите элемент(целое число):")
                        ch = input()
                        while not (ch.replace("-", "", 1)).isdigit():
                            print("Введите элемент(целое число):")
                            ch = input()
                        lst[int(ind)] = ch
                        print("Вы успешно изменили массив!")
                    
                    if deistv_izm == "2":
                        first = last = 0
                        end = len(lst) - 1
                        while int(first) >= int(last):
                            print("Введите два числа на разных строках, обозначающие номера начального и последнего элемента для изменения части массива, от 0 до ", (len(lst) - 1), ", первое число должно быть меньше второго:", sep = "")
                            first = input()
                            while not pr_ind(first, end):
                                print("Введите номер элемента, начиная с 0 и заканчивая ", (len(lst) - 1), ":", sep = "")
                                first = input()
                            last = input()
                            while not pr_ind(last, end):
                                print("Введите номер элемента, начиная с 0 и заканчивая ", (len(lst) - 1), ":", sep = "")
                                last = input()
                        last = int(last)
                        first = int(first)
                        print("Введите новую часть массива:", (last - first + 1), "целых чисел на одной строке, через пробел:")
                        part = input()
                        while (not pr(part)) and len(part.split()) != (last - first + 1):
                            print("Введите целые числа для изменения части массива на одной строке, через пробел:")
                            part = input()
                        part = list(map(int, part.split()))
                        lst[first:(last + 1)] = part
                        print("Вы успешно изменили массив!")
            
            elif deistv == "4":
                if len(lst) == 0:
                    print("Вы ещё не ввели массив!")
                else:
                    lst_s = lst.copy()
                    srt_s = selection_sort(lst_s)
                    print("После сортировки выбором:", *(srt_s[3]))
                    print("Количество сравнений:", srt_s[1])
                    print("Количество перестановок:", srt_s[2])
            
            elif deistv == "5":
                if len(lst) == 0:
                    print("Вы ещё не ввели массив!")
                else:
                    lst_b = lst.copy()
                    srt_b = bubble_sort(lst_b)
                    print("После сортировки пузырьком:", *(srt_b[3]))
                    print("Количество сравнений:", srt_b[1])
                    print("Количество перестановок:", srt_b[2])
            
            elif deistv == "6":
                if len(lst) == 0:
                    print("Вы ещё не ввели массив!")
                else:
                    lst_m = lst.copy()
                    srt_m = merge_sort(lst_m)
                    print("После сортировки слиянием:", *(srt_m[2]))
                    print("Количество сравнений:", srt_m[0])
                    print("Количество перестановок:", srt_m[1])  
            
            elif deistv == "7":
                if len(lst) == 0:
                    print("Вы ещё не ввели массив!")
                else:                
                    vivod(lst)
                    
if __name__ == "__main__":
    main()
